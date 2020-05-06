import shutil
import os
import logging

def create_directory_if_not_exists(path):
    expanded_path = os.path.expanduser(path)
    if os.path.exists(expanded_path):
        logging.warn(f"{expanded_path} already exists")
    else:
        os.makedirs(expanded_path, mode=0o755)
        logging.info(f"{expanded_path} created successfully")

def backup_file(path):
    expanded_path = os.path.expanduser(path)
    logging.info(f"Backing up {expanded_path} to {expanded_path}.bak")
    shutil.move(expanded_path, f"{expanded_path}.bak")


def update_file(source_path, destination_path):
    expanded_source_path = os.path.expanduser(source_path)
    expanded_destination_path = os.path.expanduser(destination_path)
    if os.path.exists(expanded_destination_path):
        logging.warn(f"{expanded_destination_path} already exists")
        backup_file(expanded_destination_path)
    shutil.copy2(expanded_source_path, expanded_destination_path)
    logging.info(f"{expanded_source_path} copied to {expanded_destination_path}")

