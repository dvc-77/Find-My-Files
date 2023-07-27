import os
import shutil


def move(src_file: str, dest_folder: str, base_path: str):
    file_name = os.path.basename(src_file)

    destination_path = os.path.join(base_path, dest_folder, file_name)

    # print(f"{destination_path} {file_name}")

    try:
        shutil.move(src_file, destination_path)
        return True
    except Exception as e:
        if isinstance(e, FileNotFoundError):
            print("Creating Unknown folder")
            os.makedirs(os.path.join(base_path, dest_folder), exist_ok=True)
            print("Transfering to Unknown folder")
            shutil.move(src_file, destination_path)
        return False
