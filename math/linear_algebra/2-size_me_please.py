
#!/usr/bin/env python3
def matrix_shape(matrix):
    """Returns the shape of a nested list (matrix) as a list of integers."""
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0] if len(matrix) > 0 else []
    return shape

