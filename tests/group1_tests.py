import unittest
from cyrano.groups.group1.commands import greetings
from cyrano.groups.group1.greeting_exception import GreetingException
from unittest.mock import patch


class Group1Tests(unittest.TestCase):

    @patch('builtins.print')
    def test_greet_me(self, mocked_print) -> None:
        greetings('Vladimir', False)
        mocked_print.assert_called_with("Hello Vladimir!")

    def test_greet_me_with_exception(self) -> None:
        with self.assertRaises(GreetingException) as context:
            greetings('Vladimir', True)

        self.assertEqual(str(context.exception), "Hello Vladimir!")


if __name__ == "__main__":
    unittest.main()
