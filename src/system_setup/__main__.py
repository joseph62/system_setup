from . import setups, operations
import argparse
import sys
import logging


def parse_args(args):
    parser = argparse.ArgumentParser(
        prog="system_setup", description="Setup various aspects of a Unix-like system"
    )
    parser.add_argument(
        "-i",
        "--include",
        help="List of setups to include",
        nargs="+",
        choices=[s.NAME for s in setups],
    )
    operations.add_arguments(parser)
    return parser.parse_args(args)


def run_installers(setups):
    for setup in setups:
        logging.info(f"Installing {setup.NAME}...")
        setup.install()
        logging.info(f"Installed {setup.NAME}.")


def run_cleaners(setups):
    for setup in setups:
        logging.info(f"Cleaning up {setup.NAME}...")
        setup.cleanup()
        logging.info(f"Cleaned up {setup.NAME}.")


def main(args):
    operations.configure_operations(args)

    used_setups = setups
    if args.include:
        used_setups = [s for s in setups if s.NAME in args.include]

    run_installers(used_setups)
    run_cleaners(used_setups)

    return 0


if __name__ == "__main__":
    sys.exit(main(parse_args(sys.argv[1:])))
