# 2D array operations: insert row, delete row, 2D search, and 90 degree clockwise rotation.

def display_matrix(matrix):
    if not matrix or len(matrix) == 0:
        print("Matrix is empty.")
        return
    print("Current 2D array:")
    for r in matrix:
        print(" ", r)

def insert_row(matrix, index, new_row):
    if len(matrix) > 0 and len(new_row) != len(matrix[0]):
        print(f"Error: Row length ({len(new_row)}) does not match matrix column count ({len(matrix[0])}).")
        return False
    if index < 0 or index > len(matrix):
        print(f"Error: Index {index} is out of bounds (valid range: 0 to {len(matrix)}).")
        return False
    matrix.insert(index, new_row)
    print(f"Inserted row at index {index}.")
    display_matrix(matrix)
    return True

def delete_row(matrix, index):
    if len(matrix) == 0:
        print("Error: Matrix has no rows to delete.")
        return False
    if index < 0 or index >= len(matrix):
        print(f"Error: Index {index} is out of bounds (valid range: 0 to {len(matrix) - 1}).")
        return False
    removed = matrix.pop(index)
    print(f"Deleted row {removed} at index {index}.")
    display_matrix(matrix)
    return True

def search_2d(matrix, value):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == value:
                print(f"Value {value} found at row {r}, column {c}.")
                return (r, c)
    print(f"Value {value} was not found in the 2D array.")
    return None

def rotate_90_clockwise(matrix):
    if not matrix or len(matrix) == 0:
        print("Matrix is empty, cannot rotate.")
        return matrix
    rows = len(matrix)
    cols = len(matrix[0])
    # Rotating 90 deg clockwise: element at (r, c) moves to (c, rows - 1 - r)
    rotated = [[matrix[rows - 1 - r][c] for r in range(rows)] for c in range(cols)]
    matrix.clear()
    matrix.extend(rotated)
    print("Rotated matrix 90 degrees clockwise:")
    display_matrix(matrix)
    return matrix

def main():
    try:
        r_count = int(input("Enter number of rows: ").strip())
        c_count = int(input("Enter number of columns: ").strip())
    except ValueError:
        print("Invalid dimensions. Defaulting to empty 2D array.")
        r_count, c_count = 0, 0

    matrix = []
    if r_count > 0 and c_count > 0:
        print(f"Enter {r_count} rows, each with {c_count} space-separated integers:")
        for i in range(r_count):
            row_vals = [int(x) for x in input(f"Row {i}: ").split()]
            while len(row_vals) != c_count:
                print(f"Expected {c_count} values, got {len(row_vals)}. Please enter again:")
                row_vals = [int(x) for x in input(f"Row {i}: ").split()]
            matrix.append(row_vals)

    display_matrix(matrix)

    while True:
        print("\n--- 2D Array Menu ---")
        print("1. Insert row at index")
        print("2. Delete row at index")
        print("3. Search for value")
        print("4. Rotate 90 degrees clockwise")
        print("5. Display matrix")
        print("6. Exit")

        choice = input("Enter choice (1-6): ").strip()

        if choice == '1':
            try:
                idx = int(input("Enter index to insert row at: ").strip())
                expected_len = len(matrix[0]) if matrix else None
                prompt = f"Enter row values separated by spaces" + (f" ({expected_len} values): " if expected_len else ": ")
                row_data = [int(x) for x in input(prompt).split()]
                insert_row(matrix, idx, row_data)
            except ValueError:
                print("Invalid input. Please enter valid integers.")

        elif choice == '2':
            try:
                idx = int(input("Enter row index to delete: ").strip())
                delete_row(matrix, idx)
            except ValueError:
                print("Invalid input. Please enter an integer.")

        elif choice == '3':
            try:
                val = int(input("Enter value to search: ").strip())
                search_2d(matrix, val)
            except ValueError:
                print("Invalid input. Please enter an integer.")

        elif choice == '4':
            rotate_90_clockwise(matrix)

        elif choice == '5':
            display_matrix(matrix)

        elif choice == '6':
            print("Exiting program.")
            break

        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
