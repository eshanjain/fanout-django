from django.test import TestCase
from calculator.calculator import Calculator

class MultiplicationDivisionTestCase(TestCase):
    def test_multiply_positive_numbers(self):
        self.assertEqual(Calculator.multiply(2, 3), 6)

    def test_multiply_negative_numbers(self):
        self.assertEqual(Calculator.multiply(-2, -3), 6)

    def test_divide_positive_numbers(self):
        self.assertEqual(Calculator.divide(6, 3), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            Calculator.divide(5, 0)
