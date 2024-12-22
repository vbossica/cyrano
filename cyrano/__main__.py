import sys
from typing import NoReturn
from .cyrano import Cyrano


def main() -> NoReturn:
    """
    Entry point for Cyrano
    """

    try:
        cli = Cyrano()
        exit_code = cli.invoke(sys.argv[1:])
        sys.exit(exit_code)
    except KeyboardInterrupt:
        sys.exit(1)


if __name__ == "__main__":
    main()
