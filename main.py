import os
from organizer import organize_files
from logging_util import setup_logger

if __name__ == "__main__":
    source_download_dir = input("Enter the source download directory: ").strip()
    target_directory = input("Enter the target directory: ").strip()

    if not os.path.isdir(source_download_dir):
        print("Error: Source directory not found.")
    elif not os.path.isdir(target_directory):
        print("Error: Target directory not found.")
    else:
        log_file = "organize_files.log"
        logger = setup_logger(log_file, target_directory)
        logger.info("Starting file organization process.")
        
        try:
            organize_files(source_download_dir, target_directory, logger)
            logger.info("File organization process completed.")
        except Exception as e:
            logger.error(f"An error occurred during the organization process: {str(e)}")

        print(f"Logs are stored in: {os.path.join('logs', log_file)}")
