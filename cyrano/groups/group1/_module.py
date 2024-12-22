from knack.arguments import ArgumentsContext
from knack.commands import CommandGroup


def load_commands(cli_command_loader) -> None:
    """
    Registers the module's commands.

    :param cli_command_loader: knack command loader
    """

    with CommandGroup(cli_command_loader,
                      'group1', 'cyrano.groups.group1.{}') as group:
        group.command('greetings', 'commands#greetings')


def load_arguments(cli_command_loader) -> None:
    """
    Registers the commands' arguments.

    :param cli_command_loader: knack command loader
    """

    with ArgumentsContext(cli_command_loader, 'group1') as arguments:
        arguments.argument('name', options_list='--name')
        arguments.argument('throw_exception', options_list='--throw-exception')
