from django.test import TestCase
from calculator.calculator import Calculator

class SubtractionTestCase(TestCase):
    def test_subtract_positive_numbers(self):
        self.assertEqual(Calculator.subtract(5, 3), 2)

    def test_subtract_negative_numbers(self):
        self.assertEqual(Calculator.subtract(-5, -3), -2)

    def test_subtract_mixed_numbers(self):
        self.assertEqual(Calculator.subtract(5, -3), 8)
