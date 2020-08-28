from . import filesystem, git, package_manager, process

operations = [filesystem, git, package_manager, process]


def add_arguments(parser):
    for operation in operations:
        operation.add_arguments(parser)


def configure_operations(args):
    for operation in operations:
        operation.configure_operation(args)
