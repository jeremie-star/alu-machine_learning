
#!/usr/bin/env python3
import numpy as np

"""
14-saddle_up.py
Performs matrix multiplication on two numpy.ndarrays without loops.
Returns a new matrix or None if multiplication is not possible.
"""
def np_matmul(mat1, mat2):
    """
    Perform matrix multiplication between two numpy arrays.

    Args:
        mat1 (numpy.ndarray): First matrix.
        mat2 (numpy.ndarray): Second matrix.

    Returns:
        numpy.ndarray or None: Result of mat1 x mat2 if shapes are compatible, else None.
    """
    if mat1.shape[1] != mat2.shape[0]:
        return None
    return np.matmul(mat1, mat2)

