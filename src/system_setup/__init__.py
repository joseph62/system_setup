import logging

from . import bash, git, vim, zsh, scripts

installers = [bash.install, git.install, vim.install, zsh.install, scripts.install]

cleaners = [bash.cleanup, git.cleanup, vim.cleanup, zsh.cleanup, scripts.cleanup]

logging.basicConfig(level=logging.INFO)
