# Menu-driven matrix calculator supporting addition, multiplication, transpose, and determinant.

def display_matrix(matrix, label="Matrix"):
    print(f"{label}:")
    for row in matrix:
        print(" ", row)

def read_matrix(name="Matrix"):
    rows = int(input(f"Enter number of rows for {name}: ").strip())
    cols = int(input(f"Enter number of columns for {name}: ").strip())
    print(f"Enter {rows} rows with {cols} space-separated integers each:")
    matrix = []
    for r in range(rows):
        row_vals = [int(x) for x in input(f"Row {r}: ").split()]
        while len(row_vals) != cols:
            print(f"Expected {cols} values, got {len(row_vals)}. Please enter again:")
            row_vals = [int(x) for x in input(f"Row {r}: ").split()]
        matrix.append(row_vals)
    return matrix

def add_matrices(A, B):
    rA, cA = len(A), len(A[0])
    rB, cB = len(B), len(B[0])
    if rA != rB or cA != cB:
        print(f"Error: Dimension mismatch. Cannot add {rA}x{cA} and {rB}x{cB} matrices.")
        return None
    result = [[A[r][c] + B[r][c] for c in range(cA)] for r in range(rA)]
    return result

def multiply_matrices(A, B):
    rA, cA = len(A), len(A[0])
    rB, cB = len(B), len(B[0])
    if cA != rB:
        print(f"Error: Incompatible dimensions. Cannot multiply {rA}x{cA} by {rB}x{cB} (columns of A must match rows of B).")
        return None
    result = [[0 for _ in range(cB)] for _ in range(rA)]
    for i in range(rA):
        for j in range(cB):
            result[i][j] = sum(A[i][k] * B[k][j] for k in range(cA))
    return result

def transpose_matrix(A):
    rows = len(A)
    cols = len(A[0])
    return [[A[r][c] for r in range(rows)] for c in range(cols)]

def get_submatrix(matrix, row_to_skip, col_to_skip):
    return [
        [matrix[r][c] for c in range(len(matrix)) if c != col_to_skip]
        for r in range(len(matrix)) if r != row_to_skip
    ]

def determinant(matrix):
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            print("Error: Determinant can only be calculated for square matrices.")
            return None

    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if n == 3:
        a, b, c = matrix[0]
        det = (a * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
             - b * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
             + c * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))
        return det

    det = 0
    for col in range(n):
        sub = get_submatrix(matrix, 0, col)
        sign = 1 if col % 2 == 0 else -1
        det += sign * matrix[0][col] * determinant(sub)
    return det

def main():
    while True:
        print("\n--- Matrix Calculator Menu ---")
        print("1. Add two matrices")
        print("2. Multiply two matrices")
        print("3. Transpose a matrix")
        print("4. Find determinant of a matrix")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == '1':
            try:
                A = read_matrix("Matrix A")
                B = read_matrix("Matrix B")
                display_matrix(A, "Matrix A")
                display_matrix(B, "Matrix B")
                res = add_matrices(A, B)
                if res is not None:
                    display_matrix(res, "Result of Addition (A + B)")
            except ValueError:
                print("Invalid input values.")

        elif choice == '2':
            try:
                A = read_matrix("Matrix A")
                B = read_matrix("Matrix B")
                display_matrix(A, "Matrix A")
                display_matrix(B, "Matrix B")
                res = multiply_matrices(A, B)
                if res is not None:
                    display_matrix(res, "Result of Multiplication (A x B)")
            except ValueError:
                print("Invalid input values.")

        elif choice == '3':
            try:
                A = read_matrix("Matrix")
                display_matrix(A, "Original Matrix")
                res = transpose_matrix(A)
                display_matrix(res, "Transposed Matrix")
            except ValueError:
                print("Invalid input values.")

        elif choice == '4':
            try:
                rows = int(input("Enter number of rows: ").strip())
                cols = int(input("Enter number of columns: ").strip())
                if rows != cols:
                    print(f"Error: Matrix is {rows}x{cols}. Determinant requires a square matrix.")
                    continue
                print(f"Enter {rows} rows with {cols} space-separated integers each:")
                matrix = []
                for r in range(rows):
                    row_vals = [int(x) for x in input(f"Row {r}: ").split()]
                    while len(row_vals) != cols:
                        print(f"Expected {cols} values. Re-enter row {r}:")
                        row_vals = [int(x) for x in input(f"Row {r}: ").split()]
                    matrix.append(row_vals)
                display_matrix(matrix, "Input Matrix")
                det_val = determinant(matrix)
                if det_val is not None:
                    print(f"Determinant = {det_val}")
            except ValueError:
                print("Invalid input values.")

        elif choice == '5':
            print("Exiting calculator.")
            break

        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
