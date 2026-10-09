# Lab 2 Answers

---

##  Section A: Concept Check
*Fill-in-the-blank / Short answers:*

- `list`
- `all`, `O(n)`
- `after`
- `end`
- `sequentially`, `sorted`
- `non-zero`, `row`, `column`
- `(row, column, value)`

---

##  Section B: Trace the Logic

### 1. Array Operations
- **Initial:** `[10, 20, 30, 40, 50]`
- **Insert `25` at index `2`:** `[10, 20, 25, 30, 40, 50]`
- **Delete index `0`:** `[20, 25, 30, 40, 50]`
- **Rotate left by `2`:** `[30, 40, 50, 20, 25]`

### 2. Linear Search for 19 in `[5, 12, 8, 19, 3, 27]`
- **Index 0:** `5 != 19`
- **Index 1:** `12 != 19`
- **Index 2:** `8 != 19`
- **Index 3:** `19 == 19` *(found)*
> **Indices checked:** `0, 1, 2, 3`. 
> **Result:** Found at index `3`.

### 3. Binary Search for 15 in `[2, 4, 7, 10, 15, 20, 22]`
- **Step 1:** `low = 0`, `high = 6`, `mid = 3` *(val = 10)*. `15 > 10` ➡️ `low = 4`
- **Step 2:** `low = 4`, `high = 6`, `mid = 5` *(val = 20)*. `15 < 20` ➡️ `high = 4`
- **Step 3:** `low = 4`, `high = 4`, `mid = 4` *(val = 15)*. `15 == 15` ➡️ **found at index `4`**

### 4. Sparse Triples for Matrix D
- **Non-zero triples in row-major order:** 
  `[(0, 2, 5), (1, 1, 8), (2, 0, 3)]`

### 5. Element Count Comparison for Matrix D
- **Full 2D:** `4 * 3` = **`12` values**
- **Sparse:** `3 * 3` = **`9` values**

---

## Section D: Space Optimization Analysis

### Space Complexity
- **Full 2D Matrix:** `m * n` values
- **Sparse Matrix:** `3 * k` values *(where `k` is the number of non-zero elements)*

### 6x6 Matrix Test Results
| Matrix | Sparsity | Non-Zeros | Full Space | Sparse Space | Efficiency |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Matrix 1** | ~80% zeros | `7` | `36` values | `21` values |  Saves space |
| **Matrix 2** | <20% zeros | `31` | `36` values | `93` values |  Wastes space |

### Optimization Insights
- **Cutoff Threshold:** Sparse representation stops saving space when non-zero elements exceed **~33.3%** (1/3 of the matrix). This is because each sparse entry stores 3 values (`3k >= mn`).
- **Real-World Example:** The **adjacency matrix of a social network graph**. Each person only connects to a few hundred friends out of millions of users, meaning over **99%** of entries are zero, making sparse matrices highly efficient for this use case.
- 
