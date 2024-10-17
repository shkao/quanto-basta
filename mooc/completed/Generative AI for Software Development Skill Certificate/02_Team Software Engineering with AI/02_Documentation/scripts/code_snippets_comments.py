# Example 1
def bubble_sort(arr):
    """
    Sorts the input array in ascending order using the Bubble Sort algorithm.

    Args:
        arr (list): The input array to be sorted.

    Returns:
        list: The sorted array.

    Raises:
        ValueError: If the input array is not a list.

    Example:
        >>> bubble_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    # Check if the input is a list
    if not isinstance(arr, list):
        raise ValueError("Input must be a list.")

    # Get the length of the array
    n = len(arr)

    # Iterate over the array n-1 times
    for i in range(n):
        # Iterate over the unsorted part of the array
        for j in range(0, n - i - 1):
            # If the current element is greater than the next element, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Example 2
import pandas as pd
import numpy as np

# load weather data
weather_df = pd.DataFrame("april2024_station_data.csv")

# Numpy is faster so convert
wind_speed = df["wind_speed"].to_numpy()
wind_direction = df["wind_direction"].to_numpy()

# Better built in function in np
wind_direction_rad = np.deg2rad(wind_direction)
