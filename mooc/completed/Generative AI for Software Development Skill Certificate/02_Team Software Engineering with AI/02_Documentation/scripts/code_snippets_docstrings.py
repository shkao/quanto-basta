# Example 1
def calculate_area(radius: float) -> float:
    """
    Calculates the area of a circle given its radius.

    Args:
        radius: The radius of the circle. Type: float, Required.

    Returns:
        The area of the circle. Type: float.

    Raises:
        TypeError: If the input is not a number.
    """
    if not isinstance(radius, (int, float)):
        raise TypeError("Input must be a number.")
    pi = 3.14159
    return pi * radius * radius


# Example 2
def find_max(numbers: list[float | int]) -> float:
    """
    Finds the maximum value in a list of numbers.

    Args:
        numbers: A list of numbers. Type: list[float | int], Required.

    Returns:
        The maximum value in the list. Type: float.

    Raises:
        ValueError: If the list is empty.
    """
    if len(numbers) == 0:
        raise ValueError("List cannot be empty.")
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number


# Example 3
def bubble_sort(arr: list[float | int]) -> list[float | int]:
    """
    Sorts a list using the bubble sort algorithm.

    Args:
        arr: A list of numbers. Type: list[float | int], Required.

    Returns:
        The sorted list. Type: list[float | int].

    Raises:
        TypeError: If the input is not a list.
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
