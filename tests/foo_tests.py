import unittest


class FooTests(unittest.TestCase):

    def test_foo(self) -> None:
        self.assertEqual('bar', 'bar')
