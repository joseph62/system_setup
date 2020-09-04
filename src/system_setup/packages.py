from .operations import package_manager
from .operations.package_manager import options, brew, apt, dnf, same_package

NAME = "other-packages"


def install():
    package_manager.install_program_if_not_exists(
        "rlwrap", options(*same_package("rlwrap", brew, apt, dnf))
    )
    package_manager.install_program_if_not_exists(
        "http", options(*same_package("httpie", brew, apt, dnf))
    )


def cleanup():
    pass
