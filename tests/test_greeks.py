# tests/test_greeks.py


import unittest
from src.calculator.greeks import (
    calculate_delta,
    calculate_gamma,
    calculate_vega,
    calculate_theta,
    calculate_rho
)

class TestGreeks(unittest.TestCase):
    def setUp(self):
        self.S = 100     # Stock price
        self.K = 110     # Strike price
        self.T = 30 / 365  # Time to expiration in years (30 days)
        self.r = 0.06    # Risk-free rate
        self.sigma = 0.20  # Volatility

    def test_calculate_delta_call(self):
        delta = calculate_delta(self.S, self.K, self.T, self.r, self.sigma, 'c')
        expected_delta = 0.0609  # Corrected expected value
        self.assertAlmostEqual(delta, expected_delta, places=4, msg="Call option delta calculation failed")

    def test_calculate_delta_put(self):
        delta = calculate_delta(self.S, self.K, self.T, self.r, self.sigma, 'p')
        expected_delta = -0.9391  # Corrected expected value
        self.assertAlmostEqual(delta, expected_delta, places=4, msg="Put option delta calculation failed")

    def test_calculate_gamma(self):
        gamma = calculate_gamma(self.S, self.K, self.T, self.r, self.sigma)
        expected_gamma = 0.0210  # Corrected expected value
        self.assertAlmostEqual(gamma, expected_gamma, places=4, msg="Gamma calculation failed")

    def test_calculate_vega(self):
        vega = calculate_vega(self.S, self.K, self.T, self.r, self.sigma)
        expected_vega = 0.0345  # Corrected expected value
        self.assertAlmostEqual(vega, expected_vega, places=4, msg="Vega calculation failed")

    def test_calculate_theta_call(self):
        theta = calculate_theta(self.S, self.K, self.T, self.r, self.sigma, 'c')
        expected_theta = -0.0125  # Corrected expected value
        self.assertAlmostEqual(theta, expected_theta, places=4, msg="Call option theta calculation failed")

    def test_calculate_theta_put(self):
        theta = calculate_theta(self.S, self.K, self.T, self.r, self.sigma, 'p')
        expected_theta = 0.0055  # Corrected expected value
        self.assertAlmostEqual(theta, expected_theta, places=4, msg="Put option theta calculation failed")

    def test_calculate_rho_call(self):
        rho = calculate_rho(self.S, self.K, self.T, self.r, self.sigma, 'c')
        expected_rho = 0.0049  # Corrected expected value
        self.assertAlmostEqual(rho, expected_rho, places=4, msg="Call option rho calculation failed")

    def test_calculate_rho_put(self):
        rho = calculate_rho(self.S, self.K, self.T, self.r, self.sigma, 'p')
        expected_rho = -0.0851  # Corrected expected value
        self.assertAlmostEqual(rho, expected_rho, places=4, msg="Put option rho calculation failed")

if __name__ == '__main__':
    unittest.main()
