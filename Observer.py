import time
import os, platform, winreg
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from functools import lru_cache
from Move import move


def add_to_startup() -> None:
    script_path = os.path.abspath(__file__)

    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Run",
        0,
        winreg.KEY_READ,
    )

    try:
        existing_value, _ = winreg.QueryValueEx(key, "Observe")
        if existing_value == script_path:
            print("Script is already in the startup applications.")
            return
    except WindowsError:
        pass

    n_key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Run",
        0,
        winreg.KEY_SET_VALUE,
    )

    winreg.SetValueEx(n_key, "Observe", 0, winreg.REG_SZ, script_path)

    winreg.CloseKey(key)

    print("[+] Operation complete [+]")


def MakeStartApp() -> None:
    sys_platform = platform.system()

    if sys_platform == "Windows":
        add_to_startup()


# Dictionary for extensions
All_file_extensions = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"],
    "Documents": [
        ".doc",
        ".docx",
        ".pdf",
        ".txt",
        ".rtf",
        ".odt",
        ".xls",
        ".xlsx",
        ".ppt",
        ".pptx",
    ],
    "Videos": [
        ".mp4",
        ".avi",
        ".mkv",
        ".mov",
        ".wmv",
        ".flv",
        ".webm",
        ".3gp",
        ".mpeg",
        ".mpg",
    ],
    "Audio": [".mp3", ".wav", ".ogg", ".flac", ".aac", ".wma", ".m4a"],
    "Compressed": [
        ".zip",
        ".rar",
        ".7z",
        ".tar",
        ".gz",
        ".bz2",
        ".xz",
        ".tar.gz",
        ".tar.bz2",
        ".tar.xz",
    ],
}


@lru_cache(maxsize=12)
def compareExtension(file_extension: str) -> str:
    for key, value in All_file_extensions.items():
        if file_extension in value:
            return key

    return "Unknown"


def OrganizeExisting() -> None:
    files = [
        os.path.join(folder_to_watch, x)
        for x in os.listdir(folder_to_watch)
        if os.path.isfile(os.path.join(folder_to_watch, x))
    ]

    for idx, file in enumerate(files):
        f_extension = os.path.splitext(file)[1]

        # Getting folder to transfer to
        to_folder = compareExtension(f_extension)

        move(file, to_folder, folder_to_watch)

        print(f"{idx}:  {file} moved to -> {to_folder}")


class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        file_extension = os.path.splitext(event.src_path)[1]

        # Getting Folder to Move file to
        to_folder = compareExtension(file_extension)

        # Left move function from one of the branches
        move(event.src_path, to_folder, folder_to_watch)

        # This function will be called when a new file is created in the monitored folder.
        print(f"New file added: {event.src_path} extension: {file_extension}")
        print("File moved")


if __name__ == "__main__":
    # Specify the folder you want to monitor here.
    folder_to_watch = "c:/Users/Anon/Downloads"

    # Add file to registry
    MakeStartApp()

    # Organizing folder
    OrganizeExisting()

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=folder_to_watch, recursive=False)
    observer.start()

    print("Active")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
