#!/usr/bin/env python3
"""
12-bracin_the_elements.py
Performs element-wise addition, subtraction, multiplication, and division
on two lists or scalars without using loops, conditionals, or imports.
"""


def np_elementwise(mat1, mat2):
    """
    Performs element-wise addition, subtraction, multiplication, and division.

    Args:
        mat1 (list or int/float): First list or scalar.
        mat2 (list or int/float): Second list or scalar.

    Returns:
        tuple: (sum, difference, product, quotient)
    """
    # Convert scalars to lists for broadcasting
    mat1 = mat1 if isinstance(mat1, list) else [mat1] * len(mat2)
    mat2 = mat2 if isinstance(mat2, list) else [mat2] * len(mat1)

    # Element-wise operations using list comprehensions
    add = [a + b for a, b in zip(mat1, mat2)]
    sub = [a - b for a, b in zip(mat1, mat2)]
    mul = [a * b for a, b in zip(mat1, mat2)]
    div = [a / b for a, b in zip(mat1, mat2)]

    return (add, sub, mul, div)
