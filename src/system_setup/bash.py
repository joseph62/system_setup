import logging
from .operations import filesystem

def install():
    logging.info("Installing bash...")

    filesystem.create_directory_if_not_exists("~/.local/etc/dot-files")

    logging.info("Installed bash.")
