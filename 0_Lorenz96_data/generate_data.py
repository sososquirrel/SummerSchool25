from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
import os

# These are our constants
N = 5  # Number of variables
F = 8  # Forcing
T=10000

output_pathdir = '/Users/sophieabramian/Documents/GentineLabSummer2025/0_Lorenz96_data'


def L96(x, t):
    """Lorenz 96 model with constant forcing"""
    return (np.roll(x, -1) - np.roll(x, 2)) * np.roll(x, 1) - x + F 


if __name__ == "__main__":
    x0 = F * np.ones(N)  # Initial state (equilibrium)
    x0[0] += 0.01  # Add small perturbation to the first variable
    t = np.arange(0.0, T/100, 0.01)

    x = odeint(L96, x0, t)

    output_file = f'lorenz96_N{N}_F{F}_t{len(t)}'
    output_path = os.path.join(output_pathdir, output_file)
    print(f"Saving to {output_path}")
    np.save(output_path, x)