import subprocess
import os
import logging
from . import process

def add_arguments(parser):
    pass

def configure_operation(args):
    pass

def _clone(repository, path):
    return subprocess.run(["git", "clone", repository, path])


def _update(path):
    return subprocess.run(["git", "pull", "origin"], cwd=path)


def clone_repository_if_not_exists(repository, path):
    expanded_path = os.path.expanduser(path)
    if os.path.exists(expanded_path):
        logging.warn(f"{expanded_path} already exists, updating repository.")
        git_return = _update(expanded_path)
        if process.successful_process(git_return):
            logging.info(f"{expanded_path} successfully updated")
        else:
            logging.error(f"{expanded_path} failed to update")
    else:
        git_return = _clone(repository, expanded_path)
        if process.successful_process(git_return):
            logging.info(f"{repository} successfully cloned to {expanded_path}.")
        else:
            logging.error(f"{repository} failed clone to {expanded_path}!")
