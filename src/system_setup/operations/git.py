import subprocess
import os
import logging
import process_operations

def clone_repository_if_not_exists(repository, path):
    expanded_path = os.path.expanduser(path)
    if os.exists(expanded_path):
        logging.warn(f"{expanded_path} already exists, not cloning {repository}!")
    else:
        git = subprocess.run(["git", "clone", repository])
        if process_operations.successful_process(git):
            logging.info(f"{repository} successfully cloned to {expanded_path}.")
        else:
            logging.error(f"{repository} was not successfully cloned to {expanded_path}!")
