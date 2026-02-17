import unittest

from src.main import factorial


class TestFactorial(unittest.TestCase):
    def test_factorial(self) -> None:
        # recursive cases
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(10), 3628800)

        # base cases
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)

        # negative input (exception branch)
        with self.assertRaises(ValueError):
            factorial(-1)