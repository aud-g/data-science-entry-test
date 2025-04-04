def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    return


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"
"""

Task 1 Ans
    if not isinstance(lst, list):
        return None # or raise an exception, depending on desired error handling.
    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val
    return lst

Task 2 Ans
Invoke the function "find_and_replace" using the following scenarios:
- [1, 2, 3, 4, 2, 2], 2, 5
- ["apple", "banana", "apple"], "apple", "orange"

result1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print(result1)  # Output: [1, 5, 3, 4, 5, 5]

result2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print(result2)  # Output: ['orange', 'banana', 'orange']
"""
