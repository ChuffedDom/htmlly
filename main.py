import os
import threading
import webbrowser
import socketserver
import http.server
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Label, Log, Static
from textual.containers import Container, Horizontal, Vertical
from textual import work

import slide_generator as sg

PORT = 8000

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, watch_file, html_file, on_render_callback):
        self.watch_file = os.path.abspath(watch_file)
        self.html_file = html_file
        self.on_render_callback = on_render_callback
        # Initial render
        self.render()

    def on_modified(self, event):
        if not event.is_directory and os.path.abspath(event.src_path) == self.watch_file:
            self.render()

    def render(self):
        timestamp = datetime.now().strftime('%H:%M:%S')
        try:
            with open(self.watch_file, 'r') as f:
                lines = f.readlines()

            slides = []
            current_slide_args = None

            for line in lines:
                if '$lide ' in line:
                    slide_command = line.split('$lide ', 1)[1].strip().replace(" ", "_")
                    slides.append({'command': slide_command, 'args': []})
                    current_slide_args = slides[-1]['args']
                elif current_slide_args is not None:
                    if line.strip():
                        current_slide_args.append(line.rstrip('\n'))
                    else:
                        current_slide_args = None
            
            all_slides_html = "".join(
                getattr(sg, slide['command'])(slide['args'])
                if hasattr(sg, slide['command'])
                else f"<p>Unknown command: {slide['command']}</p>"
                for slide in slides
            )

            main_template = sg.env.get_template("main.html")
            final_html = main_template.render(content=all_slides_html)

            with open(self.html_file, 'w') as f:
                f.write(final_html)
            
            self.on_render_callback(f"Rendered at {timestamp}")
        except Exception as e:
            self.on_render_callback(f"Error: {str(e)}")

class HtmllyTUI(App):
    TITLE = "Htmlly"
    SUBTITLE = "Markdown to Slide Generator"
    CSS = """
    Screen {
        align: center middle;
    }
    #main-container {
        width: 80%;
        height: 80%;
        border: thick $primary;
        padding: 1 2;
        background: $surface;
    }
    .status-label {
        margin: 1 0;
        text-style: italic;
        color: $text-muted;
    }
    #file-label {
        margin-bottom: 1;
        color: $accent;
        text-style: bold;
    }
    Log {
        height: 1fr;
        margin: 1 0;
        border: sunken $panel;
    }
    Horizontal {
        height: auto;
        align: center middle;
        margin-top: 1;
    }
    Button {
        margin: 0 1;
    }
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.observer = None
        self.httpd = None
        self.markdown_file = None
        self.html_file = None

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="main-container"):
            yield Static("Welcome to Htmlly", id="title")
            yield Label("No file selected", id="file-label")
            yield Label("Status: Ready", id="status-label", classes="status-label")
            yield Log(id="event-log")
            with Horizontal():
                yield Button("Select File", variant="primary", id="btn-select")
                yield Button("Stop & Exit", variant="error", id="btn-stop")
        yield Footer()

    def on_mount(self) -> None:
        self.query_one("#event-log").write_line("App started. Please select a Markdown file.")

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-select":
            await self.handle_select_file()
        elif event.button.id == "btn-stop":
            self.exit()

    @work(thread=True)
    def handle_select_file(self) -> None:
        # We need to run file picker in a way that works for TUI.
        # Since we are on a desktop, we can use a small python snippet to call a native picker
        # Or just ask for the path. Let's try to use a native picker if available via tkinter
        # but in a separate process/thread so it doesn't block TUI.
        import tkinter as tk
        from tkinter import filedialog
        
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(
            title="Select a Markdown File",
            filetypes=(("Markdown files", "*.md"), ("All files", "*.*"))
        )
        root.destroy()
        
        if file_path:
            self.call_from_thread(self.start_watching, file_path)

    def start_watching(self, file_path: str) -> None:
        self.markdown_file = file_path
        self.query_one("#file-label").update(f"Watching: {os.path.basename(file_path)}")
        self.query_one("#event-log").write_line(f"Selected: {file_path}")
        
        base_name, _ = os.path.splitext(self.markdown_file)
        self.html_file = f"{base_name}.html"
        file_dir = os.path.dirname(self.markdown_file)

        # Web Server Thread
        self.run_server(file_dir)
        
        # Watcher
        event_handler = FileChangeHandler(self.markdown_file, self.html_file, self.log_render)
        self.observer = Observer()
        self.observer.schedule(event_handler, path=file_dir, recursive=False)
        self.observer.start()
        
        webbrowser.open_new_tab(f"http://localhost:{PORT}/{os.path.basename(self.html_file)}")
        self.query_one("#status-label").update("Status: Running and watching...")
        self.query_one("#btn-select").disabled = True

    @work(thread=True)
    def run_server(self, directory: str) -> None:
        os.chdir(directory)
        socketserver.TCPServer.allow_reuse_address = True
        Handler = http.server.SimpleHTTPRequestHandler
        self.httpd = socketserver.TCPServer(("", PORT), Handler)
        self.query_one("#event-log").write_line(f"Server started on http://localhost:{PORT}")
        self.httpd.serve_forever()

    def log_render(self, message: str) -> None:
        self.call_from_thread(self._update_log, message)

    def _update_log(self, message: str) -> None:
        self.query_one("#event-log").write_line(message)
        if "Error" in message:
            self.query_one("#status-label").update(f"Status: {message}")
        else:
            self.query_one("#status-label").update(f"Status: {message}")

    def on_unmount(self) -> None:
        if self.observer:
            self.observer.stop()
        if self.httpd:
            self.httpd.shutdown()

if __name__ == "__main__":
    app = HtmllyTUI()
    app.run()
