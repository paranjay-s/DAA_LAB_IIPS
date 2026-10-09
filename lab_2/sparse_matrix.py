# Sparse matrix representation (triples), reconstruction, sparse addition, and space analysis.

def to_sparse(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    triples = []
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] != 0:
                triples.append((r, c, matrix[r][c]))
    return (rows, cols, triples)

def to_dense(rows, cols, triples):
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for r, c, val in triples:
        matrix[r][c] = val
    return matrix

def display_sparse(rows, cols, triples):
    print(f"Sparse representation ({rows}x{cols} matrix, {len(triples)} non-zero entries):")
    print("  Row | Col | Value")
    print("  -----------------")
    for r, c, val in triples:
        print(f"  {r:3d} | {c:3d} | {val}")
    if not triples:
        print("  (all zero entries)")

def display_dense(matrix):
    print("Full matrix:")
    for row in matrix:
        print(" ", row)

def add_sparse(sparse1, sparse2):
    r1, c1, t1 = sparse1
    r2, c2, t2 = sparse2

    if r1 != r2 or c1 != c2:
        print(f"Error: Dimension mismatch for addition ({r1}x{c1} vs {r2}x{c2}).")
        return None

    result_triples = []
    i, j = 0, 0

    while i < len(t1) and j < len(t2):
        pos1 = (t1[i][0], t1[i][1])
        pos2 = (t2[j][0], t2[j][1])

        if pos1 < pos2:
            result_triples.append(t1[i])
            i += 1
        elif pos1 > pos2:
            result_triples.append(t2[j])
            j += 1
        else:
            total = t1[i][2] + t2[j][2]
            if total != 0:
                result_triples.append((t1[i][0], t1[i][1], total))
            i += 1
            j += 1

    while i < len(t1):
        result_triples.append(t1[i])
        i += 1

    while j < len(t2):
        result_triples.append(t2[j])
        j += 1

    return (r1, c1, result_triples)

def read_matrix_from_user(name="Matrix"):
    rows = int(input(f"Enter number of rows for {name}: ").strip())
    cols = int(input(f"Enter number of columns for {name}: ").strip())
    print(f"Enter {rows} rows with {cols} space-separated values each:")
    matrix = []
    for r in range(rows):
        row_vals = [int(x) for x in input(f"Row {r}: ").split()]
        while len(row_vals) != cols:
            print(f"Expected {cols} values, got {len(row_vals)}. Re-enter row {r}:")
            row_vals = [int(x) for x in input(f"Row {r}: ").split()]
        matrix.append(row_vals)
    return matrix

def run_space_analysis():
    print("\n--- Section D: Space Optimization Analysis ---")

    # Test Matrix 1: 6x6, ~80% zeros (7 non-zero elements, 29 zeros = 80.56% zeros)
    m1 = [
        [0, 0, 5, 0, 0, 0],
        [0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0],
        [4, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0],
        [0, 0, 1, 0, 0, 7]
    ]
    r1, c1, t1 = to_sparse(m1)
    dense_count1 = r1 * c1
    sparse_count1 = len(t1) * 3

    print("Matrix 1 (~80% zeros, 6x6):")
    print("  Full matrix elements stored:", dense_count1)
    print("  Sparse triples stored (3 values per non-zero):", len(t1), "triples =", sparse_count1, "values")
    print(f"  Space saved: {dense_count1 - sparse_count1} values ({(dense_count1 - sparse_count1) / dense_count1 * 100:.1f}% reduction)")

    # Test Matrix 2: 6x6, <20% zeros (31 non-zero elements, 5 zeros = 13.89% zeros)
    m2 = [
        [1, 2, 3, 4, 5, 6],
        [7, 0, 9, 1, 2, 3],
        [4, 5, 0, 7, 8, 9],
        [1, 2, 3, 0, 5, 6],
        [7, 8, 9, 1, 0, 3],
        [4, 5, 6, 7, 8, 0]
    ]
    r2, c2, t2 = to_sparse(m2)
    dense_count2 = r2 * c2
    sparse_count2 = len(t2) * 3

    print("\nMatrix 2 (<20% zeros, 6x6):")
    print("  Full matrix elements stored:", dense_count2)
    print("  Sparse triples stored (3 values per non-zero):", len(t2), "triples =", sparse_count2, "values")
    print(f"  Sparse overhead: {sparse_count2 - dense_count2} extra values (Sparse uses more memory)")

def main():
    while True:
        print("\n--- Sparse Matrix Menu ---")
        print("1. Convert full matrix to sparse and reconstruct back")
        print("2. Add two matrices in sparse form")
        print("3. Test with worksheet Matrix D")
        print("4. Run space optimization analysis (Section D)")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == '1':
            try:
                m = read_matrix_from_user("Input Matrix")
                rows, cols, triples = to_sparse(m)
                print("\n1. Original Full Matrix:")
                display_dense(m)
                print("\n2. Converted to Sparse Representation:")
                display_sparse(rows, cols, triples)
                print("\n3. Reconstructed Back to Full Matrix:")
                reconstructed = to_dense(rows, cols, triples)
                display_dense(reconstructed)
            except ValueError:
                print("Invalid input numbers.")

        elif choice == '2':
            try:
                print("Enter First Matrix:")
                m1 = read_matrix_from_user("Matrix 1")
                print("Enter Second Matrix:")
                m2 = read_matrix_from_user("Matrix 2")

                s1 = to_sparse(m1)
                s2 = to_sparse(m2)

                print("\nSparse Matrix 1:")
                display_sparse(s1[0], s1[1], s1[2])
                print("\nSparse Matrix 2:")
                display_sparse(s2[0], s2[1], s2[2])

                res_sparse = add_sparse(s1, s2)
                if res_sparse:
                    print("\nResult of Sparse Addition (in sparse form):")
                    display_sparse(res_sparse[0], res_sparse[1], res_sparse[2])
                    print("\nResult Reconstructed as Full Matrix:")
                    res_dense = to_dense(res_sparse[0], res_sparse[1], res_sparse[2])
                    display_dense(res_dense)
            except ValueError:
                print("Invalid input numbers.")

        elif choice == '3':
            # Worksheet D matrix:
            # [[0, 0, 5],
            #  [0, 8, 0],
            #  [3, 0, 0],
            #  [0, 0, 0]]
            d_matrix = [
                [0, 0, 5],
                [0, 8, 0],
                [3, 0, 0],
                [0, 0, 0]
            ]
            print("\nWorksheet Matrix D:")
            display_dense(d_matrix)
            r, c, t = to_sparse(d_matrix)
            display_sparse(r, c, t)
            print("Row-major triples:", t)
            print(f"Full 2D representation stores: {r * c} values")
            print(f"Sparse representation stores: {len(t) * 3} values ({len(t)} triples of row, col, val)")

        elif choice == '4':
            run_space_analysis()

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
