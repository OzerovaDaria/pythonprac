import unittest
import prog

class MyTestSolver(unittest.TestCase):

    def test_zeros (self):
        self.assertEqual(prog.solve(0, 0), None)
    
    def test_zero_a (self):
        self.assertEqual(prog.solve(0, 1), None)
        
    def test_zero_b (self):
        self.assertEqual(prog.solve(1, 0), 0)
        
    def test_1 (self):
        self.assertEqual(prog.solve(1, 1), -1)

    def test_2 (self):
        self.assertEqual(prog.solve(25, -5), 0.2)

