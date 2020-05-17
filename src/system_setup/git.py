import logging

from .operations import filesystem, git

def install():
    logging.info("Installing git...")


    git.clone_repository_if_not_exists("https://github.com/joseph62/dot-files", "~/temp/dot-files")
    
    filesystem.update_file("~/temp/dot-files/resources/gitconfig", "~/.gitconfig")


    logging.info("Installed git.")

if __name__ == '__main__':
    install()
