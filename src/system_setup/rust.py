import logging
import subprocess

NAME = "rust"


def install():
    subprocess.run(
        "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh", shell=True
    )


def cleanup():
    pass
