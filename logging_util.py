import os
import logging

def setup_logger(log_file, src_dir):
    log_folder = src_dir
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    log_file_path = os.path.join(log_folder, log_file)

    logger = logging.getLogger('organize_files')
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
