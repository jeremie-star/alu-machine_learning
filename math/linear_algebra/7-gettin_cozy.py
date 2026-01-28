
#!/usr/bin/env python3
def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenates two 2D matrices along a specific axis. Returns None if not possible."""
    if axis == 0:  # Concatenate rows
        if len(mat1[0]) != len(mat2[0]):
            return None
        return mat1 + mat2
    elif axis == 1:  # Concatenate columns
        if len(mat1) != len(mat2):
            return None
        return [mat1[i] + mat2[i] for i in range(len(mat1))]

