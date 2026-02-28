import tkinter as tk
from tkinter import filedialog
import time
from datetime import datetime
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import slide_generator as sg
import http.server
import socketserver
import threading
import webbrowser

PORT = 8000



class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, watch_file, html_file):
        self.watch_file = os.path.abspath(watch_file)
        self.html_file = html_file

    def on_modified(self, event):
        if not event.is_directory and os.path.abspath(event.src_path) == self.watch_file:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"📄 [{timestamp}] File saved: {self.watch_file}")

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
                        current_slide_args.append(line.strip())
                    else:
                        # Stop collecting arguments for the current slide on a blank line
                        current_slide_args = None
            
            for slide in slides:
                command = slide['command']
                args = slide['args']
                
                if hasattr(sg, command):
                    html_output = getattr(sg, command)(args)
                    print(html_output)
                else:
                    print(f"  🤔 Unknown command: {command}")


def select_markdown_file():
    """Opens a file picker to select a markdown file."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(
        title="Select a Markdown File",
        filetypes=(("Markdown files", "*.md"), ("All files", "*.*"))
    )

    if file_path:
        print(f'Selected file: {file_path}')
    else:
        print("No file selected.")

    return file_path


if __name__ == "__main__":
    markdown_file = select_markdown_file()

    if markdown_file:
        base_name, _ = os.path.splitext(markdown_file)
        html_file = f"{base_name}.html"
        file_dir = os.path.dirname(markdown_file)

        if not os.path.exists(html_file):
            print(f"✨ Creating new HTML file: {html_file}")
            with open(html_file, 'w') as f:
                # Basic HTML structure
                f.write("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Presentation</title>
</head>
<body>
</body>
</html>""")
        else:
            print(f"📖 Opening existing HTML file: {html_file}")

        # Web server needs to run from the directory of the file
        os.chdir(file_dir)
        Handler = http.server.SimpleHTTPRequestHandler
        httpd = socketserver.TCPServer(("", PORT), Handler)
        
        server_thread = threading.Thread(target=httpd.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        print(f"🌍 Starting web server at http://localhost:{PORT}")

        webbrowser.open_new_tab(f"http://localhost:{PORT}/{os.path.basename(html_file)}")

        event_handler = FileChangeHandler(markdown_file, html_file)
        observer = Observer()
        observer.schedule(event_handler, path=file_dir, recursive=False)
        observer.start()
        print(f'Watching for changes in {markdown_file}. Press Ctrl+C to stop.')

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            print("\\nObserver stopped. Exiting.")
        httpd.shutdown()
        observer.join()
