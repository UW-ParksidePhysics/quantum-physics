import numpy as np
from wag_the_dog import wag_the_dog


def main():
    well_width = 1.0
    positions = np.linspace(0., well_width)
    k_squared = (np.pi / well_width)**2  # k_1 = pi/a ==> k_1^2 = pi^2 / a^2
    wag_range = np.linspace(0.5, 1.5, num=5)
    adjustable_coefficients = k_squared * wag_range
    initial_conditions = (0., 1.)  # psi(0), psi'(0)
    wag_the_dog('infinite square well', adjustable_coefficients, well_width, positions, initial_conditions)


if __name__ == "__main__":
    main()
