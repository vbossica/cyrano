from collections import OrderedDict
from knack.commands import CLICommandsLoader
from cyrano.groups.group1._module import (
    load_commands as load_group1_commands,
    load_arguments as load_group1_arguments
)


class CyranoCommandsLoader(CLICommandsLoader):
    """
    Specific command class loader for the application
    """

    def load_command_table(self, args) -> OrderedDict:
        load_group1_commands(self)
        return super(CyranoCommandsLoader, self).load_command_table(args)

    def load_arguments(self, command) -> None:
        load_group1_arguments(self)
        super(CyranoCommandsLoader, self).load_arguments(command)
