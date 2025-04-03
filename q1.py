def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    return


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17 
"""

Task 1 Ans
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return -1
    else:
        x, y = y, x
        print(f"Swapped values: x = {x}, y = {y}")
        return None  # Returning None as printing is the required output

# Example usage (for testing, not part of the required function):
# swap(5, 10)
# swap("apple", 10)
# swap(3.14, 2.71)
"""

Task 2 Implemention
result1 = swap("Apple", 10)
if result1 == -1:
    print("One or both inputs are not numeric.")

result2 = swap(9, 17)
if result2 == -1:
    print("One or both inputs are not numeric.")
