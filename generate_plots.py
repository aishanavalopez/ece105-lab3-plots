"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
python generate_plots.py
"""

import numpy as np


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

