# tests/test_greeks.py

import unittest
import numpy as np
from src.calculator.greeks import calculate_delta, calculate_gamma, calculate_vega, calculate_theta, calculate_rho

class TestGreeks(unittest.TestCase):

    def setUp(self):
        self.S = 100     # Stock price
        self.K = 100     # Strike price
        self.T = 1       # Time to expiration (1 year)
        self.r = 0.05    # Risk-free rate
        self.sigma = 0.2 # Volatility

    def test_call_delta(self):
        delta = calculate_delta(self.S, self.K, self.T, self.r, self.sigma, 'c')
        expected_delta = 0.6368
        self.assertAlmostEqual(delta, expected_delta, places=4, msg="Call option delta calculation failed")

    def test_put_delta(self):
        delta = calculate_delta(self.S, self.K, self.T, self.r, self.sigma, 'p')
        expected_delta = -0.3632
        self.assertAlmostEqual(delta, expected_delta, places=4, msg="Put option delta calculation failed")

    def test_gamma(self):
        gamma = calculate_gamma(self.S, self.K, self.T, self.r, self.sigma)
        expected_gamma = 0.0188
        self.assertAlmostEqual(gamma, expected_gamma, places=4, msg="Gamma calculation failed")

    def test_vega(self):
        vega = calculate_vega(self.S, self.K, self.T, self.r, self.sigma)
        expected_vega = 0.3752
        self.assertAlmostEqual(vega, expected_vega, places=4, msg="Vega calculation failed")

    def test_call_theta(self):
        theta = calculate_theta(self.S, self.K, self.T, self.r, self.sigma, 'c')
        expected_theta = -6.414
        self.assertAlmostEqual(theta, expected_theta, places=3, msg="Call option theta calculation failed")

    def test_put_theta(self):
        theta = calculate_theta(self.S, self.K, self.T, self.r, self.sigma, 'p')
        expected_theta = -1.6579
        self.assertAlmostEqual(theta, expected_theta, places=3, msg="Put option theta calculation failed")

    def test_call_rho(self):
        rho = calculate_rho(self.S, self.K, self.T, self.r, self.sigma, 'c')
        expected_rho = 0.5323
        self.assertAlmostEqual(rho, expected_rho, places=4, msg="Call option rho calculation failed")

    def test_put_rho(self):
        rho = calculate_rho(self.S, self.K, self.T, self.r, self.sigma, 'p')
        expected_rho = -0.4677
        self.assertAlmostEqual(rho, expected_rho, places=4, msg="Put option rho calculation failed")

if __name__ == "__main__":
    unittest.main()
    