from . import setups
import argparse
import sys
import logging

LOGGING_OPTIONS = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}


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
    parser.add_argument(
        "-l",
        "--logging-level",
        help="The level of logging to use. Default is INFO.",
        choices=LOGGING_OPTIONS.keys(),
        default="INFO",
    )
    return parser.parse_args(args)


def run_installers(setups):
    for setup in setups:
        logging.info(f"installing up {setup.NAME}...")
        setup.install()
        logging.info(f"installed up {setup.NAME}.")


def run_cleaners(setups):
    for setup in setups:
        logging.info(f"Cleaning up {setup.NAME}...")
        setup.cleanup()
        logging.info(f"Cleaned up {setup.NAME}.")


def main(args):
    logging.basicConfig(level=LOGGING_OPTIONS[args.logging_level])

    if args.include:
        included_setups = [s for s in setups if s.NAME in args.include]
        run_installers(included_setups)
        run_cleaners(included_setups)
    else:
        run_installers(setups)
        run_cleaners(setups)

    return 0


if __name__ == "__main__":
    sys.exit(main(parse_args(sys.argv[1:])))
