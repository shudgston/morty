"""
Unit tests
Test data are compared with results found here:
http://www.bankrate.com/calculators/mortgages/mortgage-calculator.aspx
"""

import unittest
from morty.calculators import MortgageCalculator


class MortgageCalculator200kTest(unittest.TestCase):
    """Test 200k loan, 30yrs, 6.5%"""

    def setUp(self):
        self.calc = MortgageCalculator(200000, 30, 6.50)

    def test_first_month(self):
        first = next(self.calc.get_payments())
        self.assertEqual(first.payment, 1264.14)
        self.assertEqual(first.principal, 180.80)
        self.assertEqual(first.interest, 1083.33)
        self.assertEqual(first.total_interest, 1083.33)
        self.assertEqual(first.balance, 199819.20)

    def test_last_month(self):
        last = 0
        for last in self.calc.get_payments():
            print(last)

        self.assertEqual(last.payment, 1264.14)
        self.assertEqual(last.principal, 1257.33)
        self.assertEqual(last.interest, 6.81)
        self.assertEqual(last.total_interest, 255088.98)
        self.assertEqual(last.balance, 0.00)


class MortgageCalculator500kTest(unittest.TestCase):
    """Test 500k loan, 30yrs, 3.5%"""

    def setUp(self):
        self.calc = MortgageCalculator(500000, 30, 3.50)

    def test_first_month(self):
        first = next(self.calc.get_payments())
        self.assertEqual(first.payment_number, 1)
        self.assertEqual(first.payment, 2245.22)
        self.assertEqual(first.principal, 786.89)
        self.assertEqual(first.interest, 1458.33)
        self.assertEqual(first.total_interest, 1458.33)
        self.assertEqual(first.balance, 499213.11)

    def test_last_month(self):

        last = 0
        for last in self.calc.get_payments():
            print(last)

        self.assertEqual(last.payment, 2245.22)
        self.assertEqual(last.principal, 2238.69)
        self.assertEqual(last.interest, 6.53)
        self.assertEqual(last.total_interest, 308280.44)
        self.assertEqual(last.balance, 0.00)


class MortgageCalculator15yrTest(unittest.TestCase):
    """Test 500k loan, 15yrs, 3.5%"""

    def setUp(self):
        self.calc = MortgageCalculator(500000, 15, 3.50)

    def test_first_month(self):
        first = next(self.calc.get_payments())
        self.assertEqual(first.payment_number, 1)
        self.assertEqual(first.payment, 3574.41)
        self.assertEqual(first.principal, 2116.08)
        self.assertEqual(first.interest, 1458.33)
        self.assertEqual(first.total_interest, 1458.33)
        self.assertEqual(first.balance, 497883.92)

    def test_last_month(self):

        last = 0
        for last in self.calc.get_payments():
            print(last)

        self.assertEqual(last.payment, 3574.41)
        self.assertEqual(last.principal, 3564.02)
        self.assertEqual(last.interest, 10.40)
        self.assertEqual(last.total_interest, 143394.29)
        self.assertEqual(last.balance, 0.00)
