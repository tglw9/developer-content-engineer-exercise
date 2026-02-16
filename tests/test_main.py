import unittest

from src.main import factorial


class TestFactorial(unittest.TestCase):
    def test_factorial_positive(self) -> None:
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(10), 3628800)