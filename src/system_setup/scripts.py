import logging

from .operations import filesystem, git

NAME = "scripts"


def install():
    logging.info("Installing scripts...")

    filesystem.create_directory_if_not_exists("~/temp")
    filesystem.create_directory_if_not_exists("~/.local/bin")

    git.clone_repository_if_not_exists(
        "https://github.com/joseph62/Scripts", "~/temp/Scripts"
    )

    filesystem.update_all_files("~/temp/Scripts/pyscripts", "~/.local/bin")
    filesystem.update_all_files("~/temp/Scripts/shscripts", "~/.local/bin")

    logging.info("Installed scripts.")


def cleanup():
    logging.info("Cleaning up scripts...")

    filesystem.remove_directory_if_exists("~/temp/Scripts")

    logging.info("Cleaned up scripts.")


if __name__ == "__main__":
    install()
