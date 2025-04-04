def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    return


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
"""

Task 1 Ans
if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)):
        return None # or raise an error.
if divisor == 0:
        return None # or raise an error. division by zero is undefined.
return num % divisor == 0

Task 2 Ans
result1 = check_divisibility(10, 2)
print(result1)

result2 = check_divisibility(7, 3)
print(result2)
"""
