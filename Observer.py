import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        file_extension = os.path.splitext(event.src_path)[1]
        # This function will be called when a new file is created in the monitored folder.
        print(f"New file added: {event.src_path} extension: {file_extension}")


if __name__ == "__main__":
    # Specify the folder you want to monitor here.
    folder_to_watch = "c://Users//Anon//Downloads//Test"

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=folder_to_watch, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
