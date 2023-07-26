import os
import shutil


def move(src_file: str, dest_folder: str, base_path: str):
    file_name = os.path.basename(src_file)

    destination_path = os.path.join(base_path, dest_folder, file_name)

    print(f"{destination_path} {file_name}")

    try:
        shutil.move(src_file, destination_path)
        return True
    except Exception as e:
        print("Error moving {}: {}".format(src_file, str(e)))
        return False


move(
    "c:/Users/Anon/Downloads/Test/Testme.txt",
    "Documents",
    "c:/Users/Anon/Downloads/Test",
)
