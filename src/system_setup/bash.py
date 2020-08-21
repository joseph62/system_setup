import logging
from .operations import filesystem, git

NAME = "bash"


def install():
    filesystem.create_directory_if_not_exists("~/.local/etc/dot-files")
    filesystem.create_directory_if_not_exists("~/temp")

    git.clone_repository_if_not_exists(
        "https://github.com/joseph62/dot-files", "~/temp/dot-files"
    )

    filesystem.update_file("~/temp/dot-files/aliases", "~/.local/etc/dot-files/aliases")
    filesystem.update_file(
        "~/temp/dot-files/environment", "~/.local/etc/dot-files/environment"
    )
    filesystem.update_file("~/temp/dot-files/bash_logout", "~/.bash_logout")
    filesystem.update_file("~/temp/dot-files/profile", "~/.profile")
    filesystem.update_file("~/temp/dot-files/bashrc", "~/.bashrc")


def cleanup():
    filesystem.remove_directory_if_exists("~/temp/dot-files")

