# src/calculator/greeks.py

import numpy as np
from scipy.stats import norm

def calculate_d1(S, K, T, r, sigma):
    return (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))

def calculate_d2(S, K, T, r, sigma):
    return calculate_d1(S, K, T, r, sigma) - sigma * np.sqrt(T)

def calculate_delta(S, K, T, r, sigma, option_type='c'):
    d1 = calculate_d1(S, K, T, r, sigma)
    if option_type == 'c':
        return norm.cdf(d1)
    elif option_type == 'p':
        return norm.cdf(d1) - 1
    else:
        raise ValueError("Invalid option type. Use 'c' for call or 'p' for put.")

def calculate_gamma(S, K, T, r, sigma):
    d1 = calculate_d1(S, K, T, r, sigma)
    return norm.pdf(d1) / (S * sigma * np.sqrt(T))

def calculate_vega(S, K, T, r, sigma):
    d1 = calculate_d1(S, K, T, r, sigma)
    return S * norm.pdf(d1) * np.sqrt(T) / 100

def calculate_theta(S, K, T, r, sigma, option_type='c'):
    d1 = calculate_d1(S, K, T, r, sigma)
    d2 = calculate_d2(S, K, T, r, sigma)
    term1 = - (S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))
    if option_type == 'p':
        term2 = r * K * np.exp(-r * T) * norm.cdf(-d2)
        annual_theta = term1 + term2
        daily_theta = annual_theta / 365
        return daily_theta
    else:
        raise ValueError("Invalid option type. Use 'c' for call or 'p' for put.")

def calculate_rho(S, K, T, r, sigma, option_type='c'):
    d2 = calculate_d2(S, K, T, r, sigma)
    if option_type == 'c':
        return (K * T * np.exp(-r * T) * norm.cdf(d2)) / 100
    elif option_type == 'p':
        return (-K * T * np.exp(-r * T) * norm.cdf(-d2)) / 100
    else:
        raise ValueError("Invalid option type. Use 'c' for call or 'p' for put.")
