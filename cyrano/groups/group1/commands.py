import logging
from .greeting_exception import GreetingException


def greetings(name: str, throw_exception: bool = False) -> None:
    """
    Sends greetings.

    :param name: the name to greet
    :param throw_exception: send greetings as exception
    """
    logging.info('Sending greetings')
    greeting = f'Hello {name}!'
    if throw_exception:
        raise GreetingException(greeting)
    print(greeting)
