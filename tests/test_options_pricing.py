# tests/test_options_pricing.py

import unittest
from src.calculator.options_pricing import OptionCalculator

class TestOptionCalculator(unittest.TestCase):
    def setUp(self):
        self.S = 100     # Stock price
        self.K = 110     # Strike price
        self.T = 2 / 12  # Time to expiration in years (2 months)
        self.r = 0.06    # Risk-free rate
        self.sigma = 0.20  # Volatility

    def test_calculate_call_option_price(self):
        calculator = OptionCalculator(self.S, self.K, self.T, self.r, self.sigma, 'c')
        price, _ = calculator.calculate()
        expected_price = 0.6509972826696231 # You may need to adjust this expected value
        self.assertAlmostEqual(price, expected_price, places=4, msg="Call option price calculation failed")

    def test_calculate_put_option_price(self):
        calculator = OptionCalculator(self.S, self.K, self.T, self.r, self.sigma, 'p')
        price, _ = calculator.calculate()
        expected_price = 9.556478995078123  # You may need to adjust this expected value
        self.assertAlmostEqual(price, expected_price, places=4, msg="Put option price calculation failed")

    def test_time_to_expiry_validation_lower_bound(self):
        with self.assertRaises(ValueError, msg="Time to expiry lower bound validation failed"):
            OptionCalculator(self.S, self.K, 0, self.r, self.sigma, 'c')

    def test_time_to_expiry_validation_upper_bound(self):
        with self.assertRaises(ValueError, msg="Time to expiry upper bound validation failed"):
            OptionCalculator(self.S, self.K, 4/12, self.r, self.sigma, 'c')  # 4 months

    def test_valid_time_to_expiry(self):
        try:
            OptionCalculator(self.S, self.K, 3/12, self.r, self.sigma, 'c')  # 3 months
        except ValueError:
            self.fail("OptionCalculator raised ValueError unexpectedly for 3 months expiry")

if __name__ == '__main__':
    unittest.main()