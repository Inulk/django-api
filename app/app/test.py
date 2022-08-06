"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
    """ Test Calc module """

    def test_add_numbers(self):
        """Test adding two number"""
        res = calc.add(10, 15)

        self.assertEqual(res, 25)

    def test_subtract_numbers(self):
        """Test subtracting two number"""
        res = calc.substract(10, 5)

        self.assertEqual(res, 5)
