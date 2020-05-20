import logging

from . import bash, git, vim, zsh, scripts

installers = [bash.install, git.install, vim.install, zsh.install, scripts.install]

logging.basicConfig(level=logging.INFO)
