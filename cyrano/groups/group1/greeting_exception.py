class GreetingException(Exception):
    def __init__(self, message) -> None:
        super(GreetingException, self).__init__(message)
