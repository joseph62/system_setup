import logging

from . import bash, git, vim, zsh, scripts

setups = [bash, git, vim, zsh, scripts]

logging.basicConfig(level=logging.INFO)
