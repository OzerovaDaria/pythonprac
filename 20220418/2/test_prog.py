from unittest.mock import MagicMock
from prog import SquareIO
import prog
import unittest


class TestSqEq(unittest.TestCase):

    def check(self, lst):
        SquareIO.inputCoeff = MagicMock(side_effect=lst)
        SquareIO.printResult = MagicMock()
        prog.my_solve()
        return SquareIO.printResult.call_args.args[0]

    def test_zeros(self):
        res = self.check([0, 0, 0])
        assert res == 'x принадлежит (-inf, +inf)'

    def test_zero_d(self):
        res = self.check([4, 4, 1])
        assert res == (-0.5, -0.5)

    def test_norm(self):
        res = self.check([1, 2, 1])
        assert res == (-1.0, -1.0)

    def test_pos_d(self):
        res = self.check([1, -3, 2])
        assert res == (1, 2)

    def test_neg_d(self):
        res = self.check([1, 2, 5])
        assert res == "нет решений x"

    def test_not_zero_a(self):
        res = self.check([1, 0, 0])
        assert res == (0, 0)

