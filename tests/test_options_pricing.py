# tests/test_options_pricing.py

import unittest
from parameterized import parameterized
from src.calculator.options_pricing import OptionCalculator

class TestOptionPricing(unittest.TestCase):
    
    @parameterized.expand([
        (100, 100, 1, 0.05, 0.2, 'c', 10.4506),  # Corrected expected values
        (100, 100, 1, 0.05, 0.2, 'p', 5.5735),   # Corrected expected values
        (100, 90, 1, 0.05, 0.25, 'c', 18.1408),  # Corrected expected values
        (100, 110, 1, 0.05, 0.15, 'p', 8.7111),  # Corrected expected values
    ])
    def test_option_pricing(self, S, K, T, r, sigma, option_type, expected_price):
        # Test option pricing with various parameters
        calculator = OptionCalculator(S, K, T, r, sigma, option_type)
        price, _ = calculator.calculate()
        
        # Assert the price with an acceptable tolerance
        self.assertAlmostEqual(price, expected_price, places=4, 
                               msg=f"{option_type.upper()} option price calculation failed for S={S}, K={K}, T={T}, r={r}, sigma={sigma}")

    def test_invalid_option_type(self):
        # Test invalid option type
        calculator = OptionCalculator(100, 100, 1, 0.05, 0.2, 'x')
        
        with self.assertRaises(ValueError):
            calculator.calculate()

if __name__ == "__main__":
    unittest.main()
