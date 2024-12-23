from knack.arguments import ArgumentsContext
from knack.commands import CommandGroup


def load_commands(cli_command_loader) -> None:
    """
    Registers the module's commands.

    :param cli_command_loader: knack command loader
    """

    with CommandGroup(cli_command_loader,
                      'optimize', 'cyrano.groups.optimize.{}') as group:
        group.command('experiences', 'commands#optimize_experiences')


def load_arguments(cli_command_loader) -> None:
    """
    Registers the commands' arguments.

    :param cli_command_loader: knack command loader
    """

    with ArgumentsContext(cli_command_loader, 'group1') as arguments:
        arguments.argument('experiences_file', options_list='--experiences-file')
        arguments.argument('requirements_file', options_list='--requirements-file')
        arguments.argument('output_file', options_list='--output-file')
