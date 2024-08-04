# src/calculator/greeks.py

import numpy as np
from scipy.stats import norm as si

def calculate_d1(S, K, T, r, sigma):
    return (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

def calculate_d2(S, K, T, r, sigma):
    return calculate_d1(S, K, T, r, sigma) - sigma * np.sqrt(T)

def calculate_delta(S, K, T, r, sigma, option_type):
    d1 = calculate_d1(S, K, T, r, sigma)
    if option_type == 'c':
        return si.cdf(d1)
    else:
        return -si.cdf(-d1)

def calculate_gamma(S, K, T, r, sigma):
    d1 = calculate_d1(S, K, T, r, sigma)
    return si.pdf(d1) / (S * sigma * np.sqrt(T))

def calculate_vega(S, K, T, r, sigma):
    d1 = calculate_d1(S, K, T, r, sigma)
    return S * si.pdf(d1) * np.sqrt(T) / 100  # scaled by 100 for percentage

def calculate_theta(S, K, T, r, sigma, option_type):
    d1 = calculate_d1(S, K, T, r, sigma)
    d2 = calculate_d2(S, K, T, r, sigma)
    term1 = -S * si.pdf(d1) * sigma / (2 * np.sqrt(T))
    if option_type == 'c':
        term2 = r * K * np.exp(-r * T) * si.cdf(d2)
        return (term1 - term2) / 365  # per day
    else:
        term2 = r * K * np.exp(-r * T) * si.cdf(-d2)
        return (term1 + term2) / 365  # per day

def calculate_rho(S, K, T, r, sigma, option_type):
    d2 = calculate_d2(S, K, T, r, sigma)
    if option_type == 'c':
        return K * T * np.exp(-r * T) * si.cdf(d2) / 100  # scaled by 100 for percentage
    else:
        return -K * T * np.exp(-r * T) * si.cdf(-d2) / 100  # scaled by 100 for percentage