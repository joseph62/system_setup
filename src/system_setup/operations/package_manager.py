import subprocess
import logging
import shlex
from dataclasses import dataclass
from .process import successful_process, program_exists


@dataclass
class Configuration:
    disable_package_manager: bool


CONFIGURATION = Configuration(disable_package_manager=True)


def add_arguments(parser):
    parser.add_argument(
        "--install-packages",
        help="Enable package manager installs",
        action="store_true",
    )


def configure_operation(args):
    global CONFIGURATION
    CONFIGURATION.disable_package_manager = not args.install_packages


def install_program_if_not_exists(program, package_manager_options):
    if CONFIGURATION.disable_package_manager:
        logging.info(f"Package manager disabled. Not installing {program}")
    if program_exists(program):
        logging.info(f"{program} already exists.")
    else:
        logging.info(f"{program} does not exist. Attempting to install.")
        for package_manager, command in package_manager_options.items():
            if program_exists(package_manager):
                logging.info(
                    f"Found {package_manager} on machine, attempting to install {program}"
                )
                r = subprocess.run(shlex.split(command))
                if successful_process(r):
                    logging.info(f"Successfully installed {program}")
                else:
                    logging.warn(f"Failed to install {program}")
                break
