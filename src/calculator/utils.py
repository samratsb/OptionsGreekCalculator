# src/calculator/utils.py

def validate_inputs(S, K, T, r, sigma, option_type):
    """Validate the inputs for the option calculator."""
    if S <= 0 or K <= 0 or T <= 0 or sigma <= 0:
        raise ValueError("Inputs must be positive numbers.")
    if option_type not in ["c", "p"]:
        raise ValueError("Option type must be 'c' for call or 'p' for put.")
