import os
import shutil


# Input he path you want to monitor
base_path = "c:/Users/Anon/Downloads/Test"


def move(src_file, dest_folder):
    file_name = os.path.basename(src_file)
    destination_path = os.path.join(base_path, dest_folder, file_name)

    # print(f"{destination_path} {file_name}")

    try:
        shutil.move(src_file, destination_path)
        return True
    except Exception as e:
        print("Error moving {}: {}".format(src_file, str(e)))
        return False
