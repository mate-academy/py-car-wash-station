from typing import List, Any


class Matrix:
    """
    Class for working with a square matrix of size N x N.
    """

    def __init__(self, matrix: List[List[Any]]):
        """
        Constructor that stores the 2D array and determines its size N.
        """
        self.matrix: List[List[Any]] = matrix
        # Determine the size N (since the matrix is N x N)
        self.N: int = len(matrix)

    def get_diagonal(self) -> List[Any]:
        """
        Returns the main diagonal of the matrix (elements where row index == column index).
        """
        diagonal = []
        for i in range(self.N):
            # Diagonal elements: matrix[i][i]
            diagonal.append(self.matrix[i][i])
        return diagonal

    def get_counter_diagonal(self) -> List[Any]:
        """
        Returns the anti-diagonal (or counter-diagonal) of the matrix.
        """
        counter_diagonal = []
        for i in range(self.N):
            # Anti-diagonal elements: matrix[i][N - 1 - i]
            counter_diagonal.append(self.matrix[i][self.N - 1 - i])
        return counter_diagonal

    def rotate_rows(self, number: int) -> None:
        """
        Cyclically rotates the rows of the matrix 'number' times.
        Rows pushed off the top move to the bottom.
        Modifies self.matrix in place.
        """
        if self.N == 0:
            return

        # Calculate the effective shift to avoid unnecessary operations
        shift = number % self.N

        if shift == 0:
            return

        # Cyclic rotation of rows using slicing: [shift:] + [:shift]
        self.matrix = self.matrix[shift:] + self.matrix[:shift]

    def rotate_columns(self, number: int) -> None:
        """
        Cyclically rotates the columns of the matrix 'number' times.
        Columns pushed off the left move to the right.
        Modifies self.matrix in place.
        """
        if self.N == 0:
            return

        # Calculate the effective shift
        shift = number % self.N

        if shift == 0:
            return

        new_matrix = []

        # Iterate over each row
        for row in self.matrix:
            # Cyclic rotation of elements within the current row
            # This is equivalent to shifting the columns.
            new_row = row[shift:] + row[:shift]
            new_matrix.append(new_row)

        # Update the matrix attribute with the new shifted array
        self.matrix = new_matrix

    def __repr__(self) -> str:
        """Helper method for convenient printing of the matrix."""
        # This implementation shows the matrix in a clear format
        return "\n".join(str(row) for row in self.matrix)


# --- Example Usage and Verification ---

initial_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_inst = Matrix(initial_matrix)

## 1. Diagonals
print("--- Diagonals ---")
print(f"Main diagonal: {matrix_inst.get_diagonal()}")
print(f"Counter diagonal: {matrix_inst.get_counter_diagonal()}")

## 2. Row Rotation
print("\n--- Rotate Rows (1 time) ---")
matrix_inst.rotate_rows(1)
print(matrix_inst)
# Expected: [[4, 5, 6], [7, 8, 9], [1, 2, 3]]

## 3. Column Rotation
print("\n--- Rotate Columns (1 time) ---")
matrix_inst.rotate_columns(1)
print(matrix_inst)
# Expected: [[5, 6, 4], [8, 9, 7], [2, 3, 1]]