import tkinter as tk
from tkinter import filedialog
import time
from datetime import datetime
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, watch_file):
        self.watch_file = os.path.abspath(watch_file)

    def on_modified(self, event):
        if not event.is_directory and os.path.abspath(event.src_path) == self.watch_file:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f'[{timestamp}] File saved: {self.watch_file}')


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
        event_handler = FileChangeHandler(markdown_file)
        observer = Observer()
        # Watch the directory of the file, not the file itself
        observer.schedule(event_handler, path=os.path.dirname(markdown_file), recursive=False)
        observer.start()
        print(f'Watching for changes in {markdown_file}. Press Ctrl+C to stop.')

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            print("Observer stopped. Exiting.")
        observer.join()
