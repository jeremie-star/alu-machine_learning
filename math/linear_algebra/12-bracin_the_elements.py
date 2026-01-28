#!/usr/bin/env python3
"""
12-bracin_the_elements.py
Performs element-wise addition, subtraction, multiplication, and division
on two lists or numbers without importing any modules.
"""


def np_elementwise(mat1, mat2):
    """
    Performs element-wise addition, subtraction, multiplication, and division.

    Args:
        mat1 (list or int/float): First list/matrix or scalar.
        mat2 (list or int/float): Second list/matrix or scalar.

    Returns:
        tuple: (sum, difference, product, quotient)
    """
    # Helper to determine if object is a list
    def is_list(x):
        return isinstance(x, list)

    # If both are numbers
    if not is_list(mat1) and not is_list(mat2):
        return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)

    # If one is scalar, broadcast it
    if not is_list(mat1):
        mat1 = [mat1] * len(mat2)
    if not is_list(mat2):
        mat2 = [mat2] * len(mat1)

    # Recursive element-wise operation
    add = []
    sub = []
    mul = []
    div = []

    for a, b in zip(mat1, mat2):
        if is_list(a) and is_list(b):
            res = np_elementwise(a, b)
            add.append(res[0])
            sub.append(res[1])
            mul.append(res[2])
            div.append(res[3])
        else:
            add.append(a + b)
            sub.append(a - b)
            mul.append(a * b)
            div.append(a / b)
    return (add, sub, mul, div)
