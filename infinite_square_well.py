import numpy as np
import matplotlib.pyplot as plt


def calculate_infinite_square_well_eigenfunctions(eigenfunction_positions, eigenfunction_index,
                                                  infinite_square_well_width=1.0):
    """
    :param eigenfunction_positions:  x-values in a Numpy array
    :param eigenfunction_index: n
    :param infinite_square_well_width: a
    :return: psi_n(x) from x_minimum to x_maximum
    """
    wave_number = eigenfunction_index * np.pi / infinite_square_well_width  # k_n = n * pi / a,  dim(k_n) = L^-1
    normalization_factor = np.sqrt(2 / infinite_square_well_width)  # A = sqrt(2 / a),  dim(A) = L^(-1/2)

    # psi_n(x) = A sin(k_n * x),  dim(psi_n) = dim(A) = L^(-1/2)
    infinite_square_well_eigenfunction_values = normalization_factor * np.sin(wave_number * eigenfunction_positions)

    return infinite_square_well_eigenfunction_values


def draw_infinite_square_well_potential(function_positions, infinite_square_well_width=1.0,
                                        maximum_potential_value=2.0):
    """
    :param function_positions:  x-values in a Numpy array
    :param infinite_square_well_width:  a
    :param maximum_potential_value: sets maximum V (and minimum V = -maximum V)
    :return:
    """
    minimum_position = np.min(function_positions)
    minimum_potential_position = minimum_position - 0.333 * infinite_square_well_width

    left_potential_positions = np.linspace(minimum_potential_position, minimum_position)
    left_potential_values = maximum_potential_value * np.ones(len(left_potential_positions))
    plt.fill_between(left_potential_positions, left_potential_values, -left_potential_values,
                     facecolor='gray', alpha=0.2)
    maximum_potential_position = minimum_position + 1.333 * infinite_square_well_width

    right_potential_positions = np.linspace(minimum_position + infinite_square_well_width, maximum_potential_position)
    right_potential_values = maximum_potential_value * np.ones(len(right_potential_positions))
    plt.fill_between(right_potential_positions, right_potential_values, -right_potential_values,
                     facecolor='gray', alpha=0.2)

    plt.xlim([np.min(left_potential_positions), np.max(right_potential_positions)])
    plt.ylim([-maximum_potential_value, maximum_potential_value])

    return
