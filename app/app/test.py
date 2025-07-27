""" Sample test """
from django.test import SimpleTestCase
from . import calc


class CalcTest(SimpleTestCase):
    """ Test the calc module """

    def test_add(self):
        """ Test adding two numbers """
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_sub(self):
        """ Test subtracting two numbers """
        res = calc.sub(10, 15)
        self.assertEqual(res, 5)
