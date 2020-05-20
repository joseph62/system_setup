import logging

from . import bash, git, vim, zsh

installers = [bash.install, git.install, vim.install, zsh.install]

logging.basicConfig(level=logging.INFO)
