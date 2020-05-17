import logging

from . import bash

installers = [
        bash.install
        ]

logging.basicConfig(level=logging.INFO)
