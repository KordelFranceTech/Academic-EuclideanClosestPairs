# graph.py
# Kordel France
########################################################################################################################
# This file contains a function to graph and display algorithmic efficiency data
########################################################################################################################

import matplotlib.pyplot as plt
from Lab0.config import DEBUG_MODE


def graph_runtime_data(brute_force_vals, efficient_vals, efficient_sort_vals):
    """
    Graphs the cost values of the brute-force and efficient algorithms to visually compare algorithm efficiency.
    :param brute_force_vals: list of cost values accumulated from brute force algorithm..
    :param efficient_vals: list of cost values accumulated from efficient algorithm, not including sorting costs.
    :param efficient_sort_vals: list of cost values accumulated from efficient algorithm, including sorting costs
    """
    # print values to screen to veriy they are correct
    if DEBUG_MODE:
        print(f'brute force vals: {brute_force_vals}')
        print(f'efficient vals: {efficient_vals}')
        print(f'efficient + sort vals: {efficient_sort_vals}')

    # set up the graph and plot the data
    n = [6, 10, 25, 100, 200, 200]
    plt.plot(n, brute_force_vals, label='brute-force algorithm runtime')
    plt.plot(n, efficient_vals, label='divide-and-conquer algorithm runtime (not incl. sorting)')
    plt.plot(n, efficient_sort_vals, label='divide-and-conquer algorithm runtime (incl. sorting)')
    plt.scatter(n, brute_force_vals)
    plt.scatter(n, efficient_vals)
    plt.scatter(n, efficient_sort_vals)
    plt.title('Algorithm Efficiency')
    plt.xlabel('n')
    plt.ylabel('Number of Operation (Cost)')
    plt.legend()
    plt.show()

