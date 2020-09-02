import logging

LOGGING_OPTIONS = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}


def add_arguments(parser):
    parser.add_argument(
        "-l",
        "--logging-level",
        help="The level of logging to use. Default is INFO.",
        choices=LOGGING_OPTIONS.keys(),
        default="INFO",
    )


def configure_operation(args):
    logging.basicConfig(level=LOGGING_OPTIONS[args.logging_level])
