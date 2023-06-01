import unittest

from src.pfp2023_richelbilderbeek.euler_6 import sum_square_differences


class TestEasySolutions(unittest.TestCase):
    def test_sum_square_differences(self):
         """Test 'sum_square_differences'."""
         self.assertIsNotNone(sum_square_differences.__doc__)
         self.assertRaises(TypeError, sum_square_differences, 10.5)
         self.assertEqual(2640, sum_square_differences(10))
         