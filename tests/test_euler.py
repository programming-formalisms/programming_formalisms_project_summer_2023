"""Testing Euler problems."""
import unittest

from src.pfp2023_richelbilderbeek.euler import (
    euler_1,
)


class TestEasySolutions(unittest.TestCase):

    """Class to test Euler functions.

    Tests Euler functions in src.pfp2023_richelbilderbeek.easy_solutions
    euler 1 problem.
    """

    def test_euler1(self):
        """Test Euler 1 problem: multiples of 3 or 5."""
        self.assertIsNotNone(euler_1.__doc__)
        result = 233168
        self.assertTrue(euler_1() == result)
