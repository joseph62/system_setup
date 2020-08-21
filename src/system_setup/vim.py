import logging

from .operations import filesystem, git, package_manager

NAME = "vim"


def install():
    package_manager.install_program_if_not_exists("vim", {
        "apt": "sudo apt install vim",
        "dnf": "sudo dnf install vim",
        "brew": "brew install vim"
    })

    filesystem.create_directory_if_not_exists("~/temp")
    filesystem.create_directory_if_not_exists("~/.vim/bundle")

    git.clone_repository_if_not_exists(
        "https://github.com/joseph62/dot-files", "~/temp/dot-files"
    )
    git.clone_repository_if_not_exists(
        "https://github.com/VundleVim/Vundle.vim.git", "~/.vim/bundle/Vundle.vim"
    )

    filesystem.update_file("~/temp/dot-files/vimrc", "~/.vimrc")


def cleanup():
    filesystem.remove_directory_if_exists("~/temp/dot-files")
