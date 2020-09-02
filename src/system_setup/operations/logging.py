import logging

LOGGING_OPTIONS = [logging.ERROR, logging.INFO, logging.DEBUG]


def add_arguments(parser):
    parser.add_argument(
        "-v",
        "--verbose",
        help="The level of logging to provide",
        action="count",
        default=0,
    )


def configure_operation(args):
    logging.basicConfig(level=LOGGING_OPTIONS[args.verbose % len(LOGGING_OPTIONS)])
