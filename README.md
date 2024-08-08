# European Option Pricing and Greeks Calculator

## Overview

This project provides a calculator for European option pricing and Greeks using the Black-Scholes model. The calculator allows you to compute the price of both call and put options, as well as their Greeks (Delta, Gamma, Vega, Theta, and Rho). It takes into account key parameters such as the strike price, stock price, risk-free rate, time to expiry in months, and volatility.

## Features

- **Option Pricing**: Calculate the price of European call and put options.
- **Greeks Calculation**: Compute the Greeks (Delta, Gamma, Vega, Theta, Rho) for both call and put options.
- **GUI Interface**: A graphical user interface (GUI) for easy input and calculation.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/OptionsGreekCalculator.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd OptionsGreekCalculator
    ```

3. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment:**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application:**

    ```bash
    python main.py
    ```

2. **Input the following parameters in the GUI:**

    - **Stock Price (S)**: Current price of the stock.
    - **Strike Price (K)**: Option strike price.
    - **Time to Expiry (T)**: Time to expiration in months.
    - **Risk-free Rate (r)**: Annual risk-free interest rate (as a decimal).
    - **Volatility (σ)**: Annualized standard deviation of stock returns (as a decimal).
    - **Option Type**: Select either "Call" or "Put".

3. **Click "Calculate"** to compute the option price and Greeks.

## Example

Here is an example of how to use the calculator:

- **Stock Price (S)**: 17,500
- **Strike Price (K)**: 17,700
- **Time to Expiry (T)**: 1 (1 month)
- **Risk-free Rate (r)**: 0.06 (6%)
- **Volatility (σ)**: 0.20 (20%)
- **Option Type**: Call

The GUI will display the calculated option price and Greeks for the provided parameters.

## Testing

To run unit tests for the calculator:

```bash
python -m unittest discover tests
```

Please feel free to add contributions!
