import os
import shutil
import magic

# https://stackoverflow.com/questions/43580/how-to-find-the-mime-type-of-a-file-in-python

def get_file_type(file_path):
    mime = magic.Magic(mime=True)
    file_type = mime.from_file(file_path)
    if file_path.endswith('.pkg'):
        file_type = 'application/octet-stream'
    return file_type

def organize_files(download_dir, target_dir, logger):
    moved_files = 0
    error_files = []

    for root, dirs, files in os.walk(download_dir):
        for filename in files:
            src_file = os.path.join(root, filename)
            if os.path.isfile(src_file):
                file_type = get_file_type(src_file)
                folder = file_type.split('/')[0].title()
                dest_folder = os.path.join(target_dir, folder)
                try:
                    os.makedirs(dest_folder, exist_ok=True)
                    dest_file = os.path.join(dest_folder, filename)
                    shutil.move(src_file, dest_file)
                    moved_files += 1
                    logger.info("Moved {} to {}".format(filename, dest_folder))
                except Exception as e:
                    error_files.append((filename, str(e)))
                    logger.error("Error moving {}: {}".format(filename, str(e)))

    logger.info("\n===== Summary =====")
    logger.info("Total files moved: {}".format(moved_files))
    logger.info("Errors encountered for the following files:")
    for filename, error_msg in error_files:
        logger.warning("{}: {}".format(filename, error_msg))