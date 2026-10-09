# Lab 2: Arrays and Matrices

> Implementations of 1D/2D array operations, sparse matrices, and a matrix calculator.

---

## Program 1: 1D Array Operations
**File:** `array_operations_1d.py`

- **Aim:** Insert, delete, linear search, and left/right rotate a 1D list.
- **Logic:** Validates indices against length, uses slicing with modulo for rotations, and searches sequentially.

### Tests
- **Normal Test:**
  - **Input:** `[10, 20, 30, 40, 50]` ➡️ insert `25` at `2` ➡️ delete at `0` ➡️ rotate left by `2`.
  - **Output:** `[30, 40, 50, 20, 25]`.
- **Boundary Test:** 
  - Insert at index `8` in a 3-element list.
  - **Output:** `Error: Index 8 is out of bounds.`

---

## Program 2: 2D Array Operations
**File:** `array_operations_2d.py`

- **Aim:** Row insert/delete, 2D value search, and 90-degree clockwise rotation.
- **Logic:** Checks row bounds and column length on insert. Rotation maps `[r][c]` to `[c][rows - 1 - r]`.

### Tests
- **Normal Test:**
  - **Input:** `[[1, 2, 3], [4, 5, 6]]`, rotate 90 deg.
  - **Output:** `[[4, 1], [5, 2], [6, 3]]`.
- **Boundary Test:** 
  - Insert a row with length `2` into a matrix with `3` columns.
  - **Output:** `Error: Row length does not match.`

---

## Program 3: Sparse Matrix
**File:** `sparse_matrix.py`

- **Aim:** Convert a matrix to sparse triples, reconstruct the full matrix, and add matrices in sparse form.
- **Logic:** Scans non-zero items into `(r, c, val)` triples. Addition merges sorted coordinate lists using two pointers.

### Tests
- **Normal Test:**
  - **Matrix 1:** `(0, 0, 1), (1, 1, 4)`
  - **Matrix 2:** `(0, 1, 2), (1, 1, -4)`
  - **Result:** `(0, 0, 1), (0, 1, 2)` *(zero-sum entry cancelled)*.
- **Boundary Test:** 
  - Add `2x3` and `3x3` matrices.
  - **Output:** `Error: Dimension mismatch.`

---

## Program 4: Matrix Calculator
**File:** `matrix_calculator.py`

- **Aim:** Menu-driven calculator for addition, multiplication, transpose, and determinant.
- **Logic:** Validates dimensions before math operations; uses recursive cofactor expansion for the determinant.

### Tests
- **Normal Test:**
  - **Input:** Determinant of `[[1, 2, 3], [0, 1, 4], [5, 6, 0]]`
  - **Result:** `1`.
- **Boundary Test:** 
  - Multiply `2x3` by `2x2`.
  - **Output:** `Error: Incompatible dimensions.`

---

## Section D: Summary

- **Space Complexity:** 
  - Full Matrix: `m * n`
  - Sparse Matrix: `3 * k` (where `k` is the number of non-zero elements)

### 6x6 Matrix Test
| Sparsity | Zeros | Sparse Space (Values) | Full Space (Values) |
| :--- | :--- | :--- | :--- |
| **Matrix 1** | 80% | `21` | `36` |
| **Matrix 2** | 14% | `93` | `36` |

- **Cutoff Point:** Sparse representation stops saving space when non-zero elements exceed **~33.3%** (`3k >= mn`).
- **Real-World Example:** A social network graph where each user connects to only ~500 out of millions of users is highly sparse, making sparse matrix representations essential for memory efficiency.
