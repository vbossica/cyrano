from collections import OrderedDict
from knack.commands import CLICommandsLoader
from cyrano.groups.optimize._module import (
    load_commands as load_optimize_commands,
    load_arguments as load_optimize_arguments
)


class CyranoCommandsLoader(CLICommandsLoader):
    """
    Specific command class loader for the application
    """

    def load_command_table(self, args) -> OrderedDict:
        load_optimize_commands(self)
        return super(CyranoCommandsLoader, self).load_command_table(args)

    def load_arguments(self, command) -> None:
        load_optimize_arguments(self)
        super(CyranoCommandsLoader, self).load_arguments(command)
