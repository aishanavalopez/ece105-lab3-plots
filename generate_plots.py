"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
python generate_plots.py
"""

import numpy as np
import matplotlib.pyplot as plt



def generate_data(seed):
    """Generate synthetic sensor temperature readings and timestamps.

    Parameters
    ----------
    seed : int
        Random seed used to initialize NumPy's default random number generator.

    Returns
    -------
    tuple
        A tuple containing three NumPy arrays:
        - sensor_a: 200 temperature readings from Sensor A with mean 25 and std 3.5.
        - sensor_b: 200 temperature readings from Sensor B with mean 27 and std 4.5.
        - timestamps: 200 time points uniformly distributed from 0 to 10 seconds.
    """
    rng = np.random.default_rng(seed)
    sensor_a = rng.normal(25, 3.5, 200)
    sensor_b = rng.normal(27, 4.5, 200)
    timestamps = rng.uniform(0, 10, 200)
    return sensor_a, sensor_b, timestamps


# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.


def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Plot sensor temperature readings as a scatter plot.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Temperature readings from Sensor A in Celsius, shape (200,).
    sensor_b : numpy.ndarray
        Temperature readings from Sensor B in Celsius, shape (200,).
    timestamps : numpy.ndarray
        Time values in seconds corresponding to each reading, shape (200,).
    ax : matplotlib.axes.Axes
        Axes object on which the scatter plot will be drawn.

    Returns
    -------
    None
        This function modifies the provided Axes object in place.
    """
    ax.scatter(timestamps, sensor_a, color='tab:blue', alpha=0.7, label='Sensor A')
    ax.scatter(timestamps, sensor_b, color='tab:orange', alpha=0.7, label='Sensor B')
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Sensor A and Sensor B Temperature Readings vs Time")
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.4)

# Create plot_histogram(sensor_a, sensor_b, ax) that draws an overlaid
# histogram of both sensors with 30 bins, alpha=0.5, vertical dashed
# mean lines, axis labels, title, and legend. NumPy-style docstring.
# Modifies ax in place, returns None.


def plot_histogram(sensor_a, sensor_b, ax):
    """Plot overlaid histograms of Sensor A and Sensor B temperature readings.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Temperature readings from Sensor A in Celsius, shape (200,).
    sensor_b : numpy.ndarray
        Temperature readings from Sensor B in Celsius, shape (200,).
    ax : matplotlib.axes.Axes
        Axes object on which the histogram will be drawn.

    Returns
    -------
    None
        This function modifies the provided Axes object in place.
    """
    ax.hist(sensor_a, bins=30, alpha=0.5, label='Sensor A', color='tab:blue')
    ax.hist(sensor_b, bins=30, alpha=0.5, label='Sensor B', color='tab:orange')

    ax.axvline(sensor_a.mean(), color='tab:blue', linestyle='--', linewidth=1)
    ax.axvline(sensor_b.mean(), color='tab:orange', linestyle='--', linewidth=1)

    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Frequency")
    ax.set_title("Temperature Distribution of Sensor A and Sensor B")
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.4)

# Create plot_boxplot(sensor_a, sensor_b, ax) that draws a side-by-side
# box plot comparing both sensors, labels axes, adds a horizontal dashed
# line at the overall mean, and includes a title. NumPy-style docstring.
# Modifies ax in place, returns None.

def plot_boxplot(sensor_a, sensor_b, ax):
    """Plot side-by-side box plots comparing Sensor A and Sensor B.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Temperature readings from Sensor A in Celsius, shape (200,).
    sensor_b : numpy.ndarray
        Temperature readings from Sensor B in Celsius, shape (200,).
    ax : matplotlib.axes.Axes
        Axes object on which the box plot will be drawn.

    Returns
    -------
    None
        This function modifies the provided Axes object in place.
    """
    ax.boxplot([sensor_a, sensor_b], labels=['Sensor A', 'Sensor B'])

    overall_mean = np.concatenate([sensor_a, sensor_b]).mean()
    ax.axhline(overall_mean, color='gray', linestyle='--', linewidth=1)

    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Box Plot of Sensor Temperature Readings")
    ax.grid(True, linestyle='--', alpha=0.4)


# Create a main() function that generates the data, creates a figure
# with three subplots (scatter, histogram, boxplot), calls each plotting
# function, saves the figure as 'sensor_plots.png', and returns None.
# NumPy-style docstring.



def main():
    """Generate sensor data and produce all visualizations in one figure.

    Returns
    -------
    None
        Saves the figure 'sensor_plots.png' to the current directory.
    """
    sensor_a, sensor_b, timestamps = generate_data(seed=42)

    fig, axes = plt.subplots(3, 1, figsize=(8, 12))

    plot_scatter(sensor_a, sensor_b, timestamps, axes[0])
    plot_histogram(sensor_a, sensor_b, axes[1])
    plot_boxplot(sensor_a, sensor_b, axes[2])

    fig.tight_layout()
    fig.savefig("sensor_plots.png", dpi=300)

if __name__ == "__main__":
    main()

