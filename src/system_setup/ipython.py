import logging

from .operations import filesystem, git, package_manager

NAME = "ipython"


def install():
    package_manager.install_program_if_not_exists(
        "python3",
        {
            "apt": "sudo apt install python3",
            "dnf": "sudo dnf install python3",
            "brew": "brew install python3",
        },
    )
    package_manager.install_program_if_not_exists(
        "ipython3",
        {
            "apt": "sudo apt install ipython3",
            "dnf": "sudo dnf install ipython3",
            "brew": "brew install ipython",
        },
    )
    filesystem.create_directory_if_not_exists("~/temp")
    filesystem.create_directory_if_not_exists(
        "~/.local/etc/ipython/profile_default/startup"
    )

    git.clone_repository_if_not_exists(
        "https://github.com/joseph62/dot-files", "~/temp/dot-files"
    )

    filesystem.update_file(
        "~/temp/dot-files/ipython/ipython_config.py",
        "~/.local/etc/ipython/profile_default/ipython_config.py",
    )
    filesystem.update_file(
        "~/temp/dot-files/ipython/interactive.py",
        "~/.local/etc/ipython/profile_default/startup/interactive.py",
    )
    filesystem.update_file(
        "~/temp/dot-files/environment", "~/.local/etc/dot-files/environment"
    )


def cleanup():
    filesystem.remove_directory_if_exists("~/temp/dot-files")
