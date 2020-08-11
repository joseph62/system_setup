from . import setups
import argparse
import sys


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
    return parser.parse_args(args)


def run_installers(setups):
    for setup in setups:
        setup.install()


def run_cleaners(setups):
    for setup in setups:
        setup.cleanup()


def main(args):
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
