import logging

from .operations import filesystem, git

NAME = "ipython"


def install():
    filesystem.create_directory_if_not_exists("~/temp")
    filesystem.create_directory_if_not_exists("~/.local/etc/ipython/profile_default/startup")

    git.clone_repository_if_not_exists(
        "https://github.com/joseph62/dot-files", "~/temp/dot-files"
    )

    filesystem.update_file("~/temp/dot-files/ipython/ipython_config.py", "~/.local/etc/ipython/profile_default/ipython_config.py")
    filesystem.update_file("~/temp/dot-files/ipython/interactive.py", "~/.local/etc/ipython/profile_default/startup/interactive.py")


def cleanup():
    filesystem.remove_directory_if_exists("~/temp/dot-files")


if __name__ == "__main__":
    install()
