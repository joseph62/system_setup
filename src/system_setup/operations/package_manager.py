import subprocess
import logging
import shlex
from .process import successful_process, program_exists


def install_program_if_not_exists(program, package_manager_options):
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
