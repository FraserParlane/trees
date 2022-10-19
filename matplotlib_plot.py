from data import path_clean_tree_data
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def make_matplotlib_plot():
    """
    Make a matplotlib plot of the tree data.
    """

    # Read in the data
    data = pd.read_csv(path_clean_tree_data)

    # Make the figure
    figure: plt.Figure = plt.figure(
        dpi=300
    )
    ax: plt.Axes = figure.add_subplot()

    # Get a list of the trees based on frequency
    freq = data['common_name'].value_counts()

    # Iterate through the most popular trees.
    colors = [
        "#ea5545",
        "#f46a9b",
        "#ef9b20",
        "#edbf33",
        "#ede15b",
        "#bdcf32",
        "#87bc45",
        "#27aeef",
        "#b33dc6",
    ]

    for i, color in enumerate(colors):

        # Select data
        name = freq.index[i]
        idata = data[data['common_name'] == name]

        # Plot
        ax.scatter(
            idata['lon'],
            idata['lat'],
            s=0.1,
            color=color,
            # alpha=0.5,
            zorder=i,
        )


    # Format
    ax.set_facecolor((0.1, 0.1, 0.1))
    ax.set_xticks([])
    ax.set_yticks([])
    figure.subplots_adjust(
        left=0,
        right=1,
        top=1,
        bottom=0,
    )
    for pos in ['left', 'right', 'top', 'bottom']:
        ax.spines[pos].set_visible(False)

    # Plot the trees
    ax.scatter(
        data['lon'],
        data['lat'],
        s=1,
        color='white',
        alpha=0.01,
        zorder=0,
    )

    # Save
    figure.savefig('matplotlib.png')


if __name__ == '__main__':
    make_matplotlib_plot()
