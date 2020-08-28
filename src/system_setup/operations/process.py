import subprocess


def add_arguments(parser):
    pass


def configure_operation(args):
    pass


def successful_process(process):
    return process.returncode == 0


def program_exists(program):
    return successful_process(subprocess.run(["which", program]))
