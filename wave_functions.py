import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler


def plot_wave_function(potential_name, length_scale, positions, quantum_numbers):
    """
    Plots one-dimensional wave function given name of potential, principal length scale of potential, and
    quantum numbers for which to plot
    :param potential_name:
    :param length_scale:
    :param positions:
    :param quantum_numbers:
    :return:
    """

    # Set curves to cycle through the following colors and styles
    curve_colors = ['blue', 'orange', 'green', 'red']
    curve_styles = ['solid', 'dashed', 'dashdot', 'dotted']
    style_cycler = (cycler('color', curve_colors) +
                    cycler('linestyle', curve_styles))

    # List of currently supported potentials
    supported_potentials = ['infinite square well']

    # Go through each potential
    if potential_name == supported_potentials[0]:
        from infinite_square_well import calculate_infinite_square_well_eigenfunctions, \
            draw_infinite_square_well_potential
        for quantum_number in quantum_numbers:
            function_values = calculate_infinite_square_well_eigenfunctions(positions, quantum_number,
                                                                            infinite_square_well_width=length_scale)
            plt.rc('axes', prop_cycle=style_cycler)
            plt.plot(positions, function_values)

        draw_infinite_square_well_potential(positions, infinite_square_well_width=length_scale,
                                            maximum_potential_value=2./length_scale)

    else:
        print('No potential named {} supported'.format(potential_name))
        print('Try one from this list: {}'.format([potential for potential in supported_potentials]))
        return

    # Formatting for all potentials and wave functions
    #    Draw psi = 0 line
    plt.axhline(color='black')
    #   Label axes
    plt.xlabel(r'$x$')
    plt.ylabel(r'$\psi_{n}(x)$')
    #   Make legend
    plt.legend([r'$n = $' + str(quantum_number) for quantum_number in quantum_numbers])
    #   Display figure
    plt.show()

    return
