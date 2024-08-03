# src/calculator/options_pricing.py

import numpy as np
from scipy.stats import norm
from src.calculator.greeks import calculate_delta, calculate_gamma, calculate_vega, calculate_theta, calculate_rho

class OptionCalculator:
    def __init__(self, S, K, T, r, sigma, option_type):
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.option_type = option_type
    
    def calculate(self):
        d1 = (np.log(self.S / self.K) + (self.r + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * np.sqrt(self.T))
        d2 = d1 - self.sigma * np.sqrt(self.T)
        
        if self.option_type == 'c':
            price = self.S * norm.cdf(d1) - self.K * np.exp(-self.r * self.T) * norm.cdf(d2)
        elif self.option_type == 'p':
            price = self.K * np.exp(-self.r * self.T) * norm.cdf(-d2) - self.S * norm.cdf(-d1)
        else:
            raise ValueError("Invalid option type. Use 'c' for call and 'p' for put.")

        # Calculate Greeks
        greeks = {
            'delta': calculate_delta(self.S, self.K, self.T, self.r, self.sigma, self.option_type),
            'gamma': calculate_gamma(self.S, self.K, self.T, self.r, self.sigma),
            'vega': calculate_vega(self.S, self.K, self.T, self.r, self.sigma),
            'theta': calculate_theta(self.S, self.K, self.T, self.r, self.sigma, self.option_type),
            'rho': calculate_rho(self.S, self.K, self.T, self.r, self.sigma, self.option_type)
        }

        return price, greeks
