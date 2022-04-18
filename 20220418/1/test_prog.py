import unittest
from prog import solveSquare


class TestSolveSquare(unittest.TestCase):

    def test_zeros (self):
        self.assertEqual(solveSquare(1, 0, 0), (0, 0))

    def test_zero_b (self):
        self.assertEqual(solveSquare(1, 0, 1), None)

    def test_zero_c (self):
        self.assertEqual(solveSquare(1, 2, 0), (-2, 0))

    def test_neg_d (self):
        self.assertEqual(solveSquare(1, 2, 5), None)

    def test_pos_d (self):
        self.assertEqual(solveSquare(2, 3, 1), (-1, -0.5))

    def test_zero_d(self):
        self.assertEqual(solveSquare(1, -3, -4), (-1, 4))

if __name__ == '__main__':
    unittest.main()