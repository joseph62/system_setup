import logging

from .operations import filesystem, git

NAME = "git"


def install():
    git.clone_repository_if_not_exists(
        "https://github.com/joseph62/dot-files", "~/temp/dot-files"
    )

    filesystem.update_file("~/temp/dot-files/gitconfig", "~/.gitconfig")


def cleanup():
    filesystem.remove_directory_if_exists("~/temp/dot-files")


if __name__ == "__main__":
    install()
