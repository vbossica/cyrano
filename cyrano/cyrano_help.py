from knack.help import CLIHelp
from ._version import VERSION

# pylint: disable=anomalous-backslash-in-string
# pylint: disable=import-outside-toplevel
# pylint: disable=unused-import


class CyranoHelp(CLIHelp):
    """
    Specific help class for the CLI.
    """

    def __init__(self, cli_ctx=None) -> None:
        # import command group help
        import cyrano.groups.optimize._help  # noqa: F401
        super(CyranoHelp, self).__init__(
            cli_ctx=cli_ctx,
            welcome_message=WELCOME_MESSAGE)


# Logo generation http://patorjk.com/software/taag/#p=display&h=2&v=3&f=Doom&t=cyrano
WELCOME_MESSAGE = f"""Cyrano {VERSION}
  ___ _   _ _ __ __ _ _ __   ___
 / __| | | | '__/ _` | '_ \ / _ \\
| (__| |_| | | | (_| | | | | (_) |
 \___|\__, |_|  \__,_|_| |_|\___/
       __/ |
      |___/

Use `cyrano -h` to see available commands.

Available commands:"""

# pylint: enable=anomalous-backslash-in-string
# pylint: enable=import-outside-toplevel
# pylint: enable=unused-import
