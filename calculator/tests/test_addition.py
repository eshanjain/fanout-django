from django.test import TestCase
from calculator.calculator import Calculator

class AdditionTestCase(TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(Calculator.add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(Calculator.add(-2, -3), -5)

    def test_add_mixed_numbers(self):
        self.assertEqual(Calculator.add(-2, 3), 1)
