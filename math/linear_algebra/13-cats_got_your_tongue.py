#!/usr/bin/env python3
"""
14-saddle_up.py
Performs matrix multiplication on two numpy.ndarrays without loops.
Returns a new matrix or None if multiplication is not possible.
"""
import numpy as np

def np_cat(mat1, mat2, axis=0):

    """Concatenates two numpy arrays along a specified axis."""
    return np.concatenate((mat1, mat2), axis=axis)
