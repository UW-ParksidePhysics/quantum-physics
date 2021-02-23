# from discrete_probability import calculate_age_distribution_properties
import numpy as np
from wave_functions import plot_wave_function


def main():
    # calculate_age_distribution_properties()
    well_width = 1.0
    positions = np.linspace(0., well_width)
    quantum_numbers = np.arange(1, 4)
    plot_wave_function('infinite square well', well_width, positions, quantum_numbers)
    # plot_wave_function('harmonic oscillator', well_width, positions, quantum_numbers)
    print()


if __name__ == "__main__":
    main()
