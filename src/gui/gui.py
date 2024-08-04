# src/gui/gui.py


import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
from src.calculator.options_pricing import OptionCalculator


class OptionsGreekCalculator:
    def __init__(self):
        self.root = ttk.Window(themename="superhero")
        self.root.title("Options Greek Calculator")
        self.root.geometry("650x450")  # Adjusted height for better layout

        self.create_widgets()

    def create_widgets(self):
        # Main Frame
        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.pack(fill='both', expand=True)

        # Labels and Entry Widgets
        self.label_S = ttk.Label(self.frame, text="Stock Price (S):")
        self.label_S.grid(row=0, column=0, pady=5, sticky=W)
        self.entry_S = ttk.Entry(self.frame)
        self.entry_S.grid(row=0, column=1, pady=5)

        self.label_K = ttk.Label(self.frame, text="Strike Price (K):")
        self.label_K.grid(row=1, column=0, pady=5, sticky=W)
        self.entry_K = ttk.Entry(self.frame)
        self.entry_K.grid(row=1, column=1, pady=5)

        self.label_T = ttk.Label(self.frame, text="Time to Expiry (T in months):")
        self.label_T.grid(row=2, column=0, pady=5, sticky=W)
        self.entry_T = ttk.Entry(self.frame)
        self.entry_T.grid(row=2, column=1, pady=5)

        self.label_r = ttk.Label(self.frame, text="Risk-free Rate (r):")
        self.label_r.grid(row=3, column=0, pady=5, sticky=W)
        self.entry_r = ttk.Entry(self.frame)
        self.entry_r.grid(row=3, column=1, pady=5)

        self.label_sigma = ttk.Label(self.frame, text="Volatility (σ):")
        self.label_sigma.grid(row=4, column=0, pady=5, sticky=W)
        self.entry_sigma = ttk.Entry(self.frame)
        self.entry_sigma.grid(row=4, column=1, pady=5)

        # Option Type Selector
        self.option_type = ttk.Combobox(self.frame, values=["Call", "Put"], state="readonly")
        self.option_type.set("Call")
        self.option_type.grid(row=5, column=1, pady=10)

        # Calculate Button
        self.calculate_button = ttk.Button(self.frame, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=6, columnspan=4, pady=15)

        # Output Label
        self.output_label = ttk.Label(self.root, text="", font=("Helvetica", 10), anchor="center", justify=CENTER)
        self.output_label.pack(pady=10, fill='x')

    def calculate(self):
        try:
            # Get user input from entry fields
            S = float(self.entry_S.get())
            K = float(self.entry_K.get())
            T_months = float(self.entry_T.get())  # Time to expiry in months
            if T_months > 3:
                raise ValueError("Time to expiry cannot be more than 3 months.")
            T = T_months / 12  # Convert months to years

            r = float(self.entry_r.get())
            sigma = float(self.entry_sigma.get())
            option_type = 'c' if self.option_type.get() == "Call" else 'p'

            # Calculate using OptionCalculator
            calculator = OptionCalculator(S, K, T, r, sigma, option_type)
            price, greeks = calculator.calculate()

            # Format the output with prices and Greeks
            output = (f"Option Price: {price:.2f}\n"
                      f"Delta: {greeks['delta']:.2f}\n"
                      f"Gamma: {greeks['gamma']:.4f}\n"
                      f"Vega: {greeks['vega']:.2f}\n"
                      f"Theta: {greeks['theta']:.2f}\n"
                      f"Rho: {greeks['rho']:.2f}")

            self.output_label.config(text=output)

        except ValueError as ve:
            Messagebox.show_error(title="Input Error", message=f"Invalid input: {str(ve)}")
        except Exception as e:
            Messagebox.show_error(title="Error", message=f"An unexpected error occurred: {str(e)}")

    def run(self):
        self.root.mainloop() # Start the tkinter app