# src/calculator/options_pricing.py

import numpy as np
from scipy.stats import norm
from .greeks import (
    calculate_delta,
    calculate_gamma,
    calculate_vega,
    calculate_theta,
    calculate_rho,
    calculate_d1,
    calculate_d2,
)


class OptionCalculator:
    def __init__(self, S, K, T, r, sigma, option_type='c'):
        if T <= 0 or T > 3/12:  # T is in years, so 3/12 is 3 months
            raise ValueError("Time to expiry must be positive and not more than 3 months")
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.option_type = option_type

    def calculate(self):
        """Calculate the option price and Greeks."""
        delta = calculate_delta(self.S, self.K, self.T, self.r, self.sigma, self.option_type)
        gamma = calculate_gamma(self.S, self.K, self.T, self.r, self.sigma)
        vega = calculate_vega(self.S, self.K, self.T, self.r, self.sigma)
        theta = calculate_theta(self.S, self.K, self.T, self.r, self.sigma, self.option_type)
        rho = calculate_rho(self.S, self.K, self.T, self.r, self.sigma, self.option_type)

        greeks = {
            'delta': delta,
            'gamma': gamma,
            'theta': theta,
            'vega': vega,
            'rho': rho
        }

        # Calculate the option price using Black-Scholes formula
        d1 = calculate_d1(self.S, self.K, self.T, self.r, self.sigma)
        d2 = calculate_d2(self.S, self.K, self.T, self.r, self.sigma)

        if self.option_type == 'c':
            price = (self.S * norm.cdf(d1) -
                     self.K * np.exp(-self.r * self.T) * norm.cdf(d2))
        else:
            price = (self.K * np.exp(-self.r * self.T) * norm.cdf(-d2) -
                     self.S * norm.cdf(-d1))

        return price, greeks
