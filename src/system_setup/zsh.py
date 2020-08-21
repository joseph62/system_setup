import logging

from .operations import filesystem, git

NAME = "zsh"


def install():
    filesystem.create_directory_if_not_exists("~/temp")
    filesystem.create_directory_if_not_exists("~/.local/opt")
    filesystem.create_directory_if_not_exists("~/.local/etc/dot-files")

    git.clone_repository_if_not_exists(
        "https://github.com/joseph62/dot-files.git", "~/temp/dot-files"
    )
    git.clone_repository_if_not_exists(
        "https://github.com/zsh-users/zsh-syntax-highlighting.git",
        "~/.local/opt/zsh-syntax-highlighting",
    )
    git.clone_repository_if_not_exists(
        "https://github.com/ohmyzsh/ohmyzsh.git", "~/.local/opt/ohmyzsh"
    )

    filesystem.update_file("~/temp/dot-files/aliases", "~/.local/etc/dot-files/aliases")
    filesystem.update_file(
        "~/temp/dot-files/environment", "~/.local/etc/dot-files/environment"
    )
    filesystem.update_file("~/temp/dot-files/zshrc", "~/.zshrc")


def cleanup():
    filesystem.remove_directory_if_exists("~/temp/dot-files")

