import logging

from .operations import filesystem, git, package_manager
from .operations.package_manager import options, same_package, brew, apt, dnf

NAME = "ipython"


def install():
    package_manager.install_program_if_not_exists(
        "python3", options(*same_package("python3", brew, apt, dnf))
    )
    package_manager.install_program_if_not_exists(
        "ipython", options(brew("ipython"), *same_package("ipython3", apt, dnf))
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
