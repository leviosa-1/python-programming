import numpy as np

def add_matrices(matrix1, matrix2):
    # Convert input matrices to numpy arrays
    array1 = np.array(matrix1)
    array2 = np.array(matrix2)

    # Check if the matrices have the same shape
    if array1.shape != array2.shape:
        raise ValueError("Matrices must have the same shape for addition.")

    # Perform matrix addition
    result = array1 + array2

    return result

# Example matrices
matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

try:
    # Call the function to add matrices
    result_matrix = add_matrices(matrix_a, matrix_b)

    # Display the result
    print("Matrix A:")
    print(np.array(matrix_a))
    print("\nMatrix B:")
    print(np.array(matrix_b))
    print("\nResultant Matrix:")
    print(result_matrix)

except ValueError as e:
    print(f"Error: {e}")
