import os
import threading
import webbrowser
import socketserver
import http.server
import logging
import traceback
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Label, Log, Static, DirectoryTree
from textual.containers import Container, Horizontal, Vertical, Grid
from textual import work
from textual.screen import ModalScreen
from pathlib import Path

import slide_generator as sg

PORT = 8000
LOG_FILE = "htmlly.log"

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_to_file(message, level="info"):
    if level == "error":
        logging.error(message)
    elif level == "debug":
        logging.debug(message)
    else:
        logging.info(message)

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, watch_file, html_file, on_render_callback):
        self.watch_file = os.path.abspath(watch_file)
        self.html_file = html_file
        self.on_render_callback = on_render_callback
        self.render()

    def on_modified(self, event):
        if not event.is_directory and os.path.abspath(event.src_path) == self.watch_file:
            self.render()

    def render(self):
        timestamp = datetime.now().strftime('%H:%M:%S')
        try:
            log_to_file(f"Starting render for {self.watch_file}")
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
            log_to_file(f"Render successful for {self.watch_file}")
        except Exception as e:
            err_msg = f"Render Error: {str(e)}\n{traceback.format_exc()}"
            self.on_render_callback(f"Error: {str(e)}")
            log_to_file(err_msg, "error")

class FilePickerScreen(ModalScreen[Path]):
    """A screen to pick a file."""
    def compose(self) -> ComposeResult:
        with Vertical(id="picker-container"):
            yield Static("Select a Markdown File", id="picker-title")
            # Set root to home directory to allow navigation
            yield DirectoryTree(str(Path.home()), id="dir-tree")
            with Horizontal(id="picker-buttons"):
                yield Button("Cancel", variant="error", id="cancel")

    def on_mount(self) -> None:
        self.query_one("#dir-tree").focus()

    def on_directory_tree_file_selected(self, event: DirectoryTree.FileSelected) -> None:
        if event.path.suffix == ".md":
            self.dismiss(event.path)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "cancel":
            self.dismiss(None)

class HtmllyTUI(App):
    TITLE = "Htmlly"
    SUBTITLE = "Markdown to Slide Generator"
    CSS = """
    Screen {
        background: $surface;
    }
    #main-container {
        height: 100%;
        padding: 0 1;
    }
    #header-area {
        height: auto;
        border-bottom: solid $primary;
        margin-bottom: 0;
        padding: 1 0;
    }
    #title {
        text-align: center;
        text-style: bold;
        width: 100%;
        color: $accent;
    }
    .status-label {
        color: $text-muted;
    }
    #file-label {
        color: $primary;
        text-style: bold;
        margin-top: 1;
    }
    #log-container {
        height: 1fr;
        border: round $panel;
        margin: 0;
    }
    Log {
        height: 100%;
    }
    #footer-buttons {
        height: auto;
        align: center middle;
    }
    Button {
        margin: 0 1;
    }

    /* Modal Styles */
    #picker-container {
        width: 60%;
        height: 70%;
        background: $surface;
        border: thick $primary;
        align: center middle;
        padding: 1;
    }
    #picker-title {
        text-align: center;
        margin-bottom: 1;
        text-style: bold;
    }
    #dir-tree {
        height: 1fr;
        border: round $panel;
    }
    #picker-buttons {
        height: auto;
        align: center middle;
        margin-top: 1;
    }
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.observer = None
        self.httpd = None
        self.markdown_file = None
        self.html_file = None

    def compose(self) -> ComposeResult:
        with Vertical(id="main-container"):
            with Vertical(id="header-area"):
                yield Static("Htmlly Control Panel", id="title")
                yield Label("No file selected", id="file-label")
                yield Label("Status: Ready", id="status-label", classes="status-label")
            
            with Container(id="log-container"):
                yield Log(id="event-log")
            
            with Horizontal(id="footer-buttons"):
                yield Button("Select File", variant="primary", id="btn-select")
                yield Button("Stop & Exit", variant="error", id="btn-stop")

    def on_mount(self) -> None:
        self.log_message("App started. Click 'Select File' to begin.")
        log_to_file("TUI mounted and ready")

    def log_message(self, message: str) -> None:
        try:
            self.query_one("#event-log").write_line(message)
            log_to_file(message)
        except Exception:
            log_to_file(f"Failed to write to TUI log: {message}", "error")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        log_to_file(f"Button pressed: {event.button.id}")
        if event.button.id == "btn-select":
            self.push_screen(FilePickerScreen(), self.handle_file_selected)
        elif event.button.id == "btn-stop":
            log_to_file("Stop button pressed, exiting")
            self.exit()

    def handle_file_selected(self, file_path: Path | None) -> None:
        if file_path:
            log_to_file(f"File selected via picker: {file_path}")
            self.start_watching(str(file_path))
        else:
            log_to_file("File selection cancelled")

    def start_watching(self, file_path: str) -> None:
        try:
            self.markdown_file = file_path
            self.query_one("#file-label").update(f"Watching: {os.path.basename(file_path)}")
            self.log_message(f"Selected: {file_path}")
            
            base_name, _ = os.path.splitext(self.markdown_file)
            self.html_file = f"{base_name}.html"
            file_dir = os.path.dirname(os.path.abspath(self.markdown_file))

            # Start Web Server Thread
            self.run_server(file_dir)
            
            # Start Watcher
            event_handler = FileChangeHandler(self.markdown_file, self.html_file, self.log_message_from_thread)
            self.observer = Observer()
            self.observer.schedule(event_handler, path=file_dir, recursive=False)
            self.observer.start()
            
            webbrowser.open_new_tab(f"http://localhost:{PORT}/{os.path.basename(self.html_file)}")
            self.query_one("#status-label").update("Status: Running and watching...")
            self.query_one("#btn-select").disabled = True
            log_to_file(f"Watcher and server started for {file_path}")
        except Exception as e:
            err_msg = f"Failed to start watching: {str(e)}\n{traceback.format_exc()}"
            log_to_file(err_msg, "error")
            self.log_message(f"Error: {str(e)}")

    @work(thread=True)
    def run_server(self, directory: str) -> None:
        try:
            log_to_file(f"Starting server in {directory}")
            os.chdir(directory)
            socketserver.TCPServer.allow_reuse_address = True
            Handler = http.server.SimpleHTTPRequestHandler
            self.httpd = socketserver.TCPServer(("", PORT), Handler)
            self.log_message_from_thread(f"Server started on http://localhost:{PORT}")
            self.httpd.serve_forever()
        except Exception as e:
            err_msg = f"Server Error: {str(e)}\n{traceback.format_exc()}"
            log_to_file(err_msg, "error")
            self.log_message_from_thread(f"Server Error: {e}")

    def log_message_from_thread(self, message: str) -> None:
        # Check if we are already in the main thread (where the app runs)
        if threading.current_thread() is threading.main_thread():
            self.log_message(message)
        else:
            self.call_from_thread(self.log_message, message)

    def on_unmount(self) -> None:
        log_to_file("Unmounting app")
        if self.observer:
            self.observer.stop()
        if self.httpd:
            threading.Thread(target=self.httpd.shutdown).start()
        log_to_file("App unmounted")

if __name__ == "__main__":
    try:
        log_to_file("--- Application Session Start ---")
        app = HtmllyTUI()
        app.run()
    except Exception as e:
        fatal_msg = f"FATAL ERROR: {str(e)}\n{traceback.format_exc()}"
        log_to_file(fatal_msg, "error")
        # Ensure the error is visible in terminal if TUI crashed
        print(fatal_msg)
