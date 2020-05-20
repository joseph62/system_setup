import logging

from .operations import filesystem, git


def install():
    logging.info("Installing git...")

    git.clone_repository_if_not_exists(
        "https://github.com/joseph62/dot-files", "~/temp/dot-files"
    )

    filesystem.update_file("~/temp/dot-files/gitconfig", "~/.gitconfig")

    logging.info("Installed git.")


def cleanup():
    logging.info("Cleaning up git...")

    filesystem.remove_directory_if_exists("~/temp/dot-files")

    logging.info("Cleaned up git.")


if __name__ == "__main__":
    install()
