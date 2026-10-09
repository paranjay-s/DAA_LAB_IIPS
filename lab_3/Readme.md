## Section A: Concept Check
1. Bubble sort works by repeatedly swapping **adjacent** elements if they are in the wrong order[span_0](start_span)[span_0](end_span).
2. Selection sort repeatedly finds the **minimum** element from the unsorted part and places it at the beginning[span_1](start_span)[span_1](end_span).
3. Insertion sort builds the sorted portion one element at a time by **inserting** each new element into its correct position[span_2](start_span)[span_2](end_span).
4. Merge sort follows a **divide** and **conquer** approach: split the array, sort each half, then combine[span_3](start_span)[span_3](end_span).
5. Quick sort picks a **pivot** and partitions the array around it before recursing[span_4](start_span)[span_4](end_span).
6. Heap sort relies on a data structure called a **heap**, which is typically implemented using an array[span_5](start_span)[span_5](end_span).
7. Radix sort processes numbers digit by digit, starting from the **least** significant digit (in the standard LSD version)[span_6](start_span)[span_6](end_span).
8. Binary search requires the input array to be **sorted** before it can be used[span_7](start_span)[span_7](end_span).
9. In hashing, when two different keys map to the same index, this is called a **collision**[span_8](start_span)[span_8](end_span).
10. Separate chaining resolves collisions by storing multiple values at the same index using a **linked list/array**, while linear probing resolves them by **finding the next available empty slot**[span_9](start_span)[span_9](end_span).

## Section B: Trace the Logic
* **1. Bubble Sort [5, 2, 8, 1, 9] (Pass 1):** [2, 5, 8, 1, 9] $\rightarrow$ [2, 5, 8, 1, 9] $\rightarrow$ [2, 5, 1, 8, 9] $\rightarrow$ [2, 5, 1, 8, 9][span_10](start_span)[span_10](end_span).
* **2. Selection Sort [5, 2, 8, 1, 9]:** Swap 1/5: [1, 2, 8, 5, 9] $\rightarrow$ Swap 2/2: [1, 2, 8, 5, 9] $\rightarrow$ Swap 5/8: [1, 2, 5, 8, 9] $\rightarrow$ Swap 8/8: [1, 2, 5, 8, 9][span_11](start_span)[span_11](end_span).
* **3. Insertion Sort [5, 2, 8, 1, 9]:** Insert 2: [2, 5, 8, 1, 9] $\rightarrow$ Insert 8: [2, 5, 8, 1, 9] $\rightarrow$ Insert 1: [1, 2, 5, 8, 9] $\rightarrow$ Insert 9: [1, 2, 5, 8, 9][span_12](start_span)[span_12](end_span).
* **4. Merge Sort Splitting [8, 3, 5, 4, 7, 6, 1, 2]:** [8, 3, 5, 4], [7, 6, 1, 2] $\rightarrow$ [8, 3], [5, 4], [7, 6], [1, 2] $\rightarrow$ [8], [3], [5], [4], [7], [6], [1], [2][span_13](start_span)[span_13](end_span).
* **5. Quick Sort Partition [8, 3, 5, 4, 7, 6, 1, 2] (Pivot 2):** Array becomes [1, 2, 5, 4, 7, 6, 8, 3]. Pivot final index is 1[span_14](start_span)[span_14](end_span).
* **6. Radix Sort [170, 45, 75, 90, 802, 24, 2, 66]:** Ones: [170, 90, 802, 2, 24, 45, 75, 66]. Tens: [802, 2, 24, 45, 66, 170, 75, 90][span_15](start_span)[span_15](end_span).
* **7. Binary Search for 23 on [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]:** low=0, high=10, mid=5. Value at mid is 23. Target found in 1 step[span_16](start_span)[span_16](end_span).
* **8. Hash Table (Separate Chaining):** Index 2: [9]. Index 3: [10 $\rightarrow$ 3 $\rightarrow$ 17 $\rightarrow$ 24][span_17](start_span)[span_17](end_span).
* **9. Hash Table (Linear Probing):** Index 2: 9. Index 3: 10. Index 4: 3. Index 5: 17. Index 6: 24[span_18](start_span)[span_18](end_span).

## Section C: Programs to Write

### Program 1: Bubble, Selection, Insertion Sort
* **Aim:** Implement and visualize basic $O(n^2)$ sorting algorithms[span_19](start_span)[span_19](end_span).
* **Logic:** Bubble swaps adjacent out-of-order items. Selection swaps the unsorted minimum with the first unsorted position. Insertion builds a sorted left half by shifting items[span_20](start_span)[span_20](end_span).
* **Sample Input:** `5 2 8 1 9`
* **Sample Output:** Traced intermediate steps and final array `[1, 2, 5, 8, 9]`.

### Program 2: Merge, Quick, Heap Sort
* **Aim:** Implement advanced divide-and-conquer and heap-based sorts[span_21](start_span)[span_21](end_span).
* **Logic:** Merge divides perfectly and combines. Quick partitions using the last element as a pivot. Heap builds a max-heap to continuously extract the largest element[span_22](start_span)[span_22](end_span).
* **Sample Input:** `8 3 5 4 7 6 1 2`
* **Sample Output:** Final sorted array `[1, 2, 3, 4, 5, 6, 7, 8]`.

### Program 3: Radix Sort
* **Aim:** Sort non-negative integers using a non-comparative LSD approach[span_23](start_span)[span_23](end_span).
* **Logic:** Uses counting sort repeatedly for each digit place (ones, tens, hundreds)[span_24](start_span)[span_24](end_span).
* **Sample Input:** `170 45 75 90 802 24 2 66`
* **Sample Output:** `[2, 24, 45, 66, 75, 90, 170, 802]`

### Program 4: Binary Search
* **Aim:** Iteratively search for an element in a pre-sorted array[span_25](start_span)[span_25](end_span).
* **Logic:** Continually halves the search interval by comparing the target with the middle element[span_26](start_span)[span_26](end_span).
* **Sample Input:** Array: `2 5 8 12 16`, Target: `8`
* **Sample Output:** `Index of 8: 2`

## Section D: Empirical Timing Analysis
* **Aim:** Compare execution times of six sorting algorithms across different input states (random, sorted, reverse-sorted) and sizes[span_27](start_span)[span_27](end_span)[span_28](start_span)[span_28](end_span).
* **Logic:** Measure `time.perf_counter()` deltas for each dataset, exporting to a CSV and plotting via Matplotlib[span_29](start_span)[span_29](end_span).
* **Sample Input:** Auto-generated arrays at `N = [100, 500, 1000, 2000]`.
* **Sample Output:** 
  * `timing_data.csv` containing numerical results.
  * `graph_random_input.png` showing distinct $O(n^2)$ curves vs $O(n \log n)$ flat lines.

## Section E: Applications

### Program 7: Student Record Manager
* **Aim:** Manage a dictionary list of students with capabilities to sort and search by distinct keys (roll, name, marks)[span_30](start_span)[span_30](end_span).
* **Logic:** Extends Merge/Bubble sort to handle dictionary keys. Calculates real-time performance difference between algorithms on the same dataset[span_31](start_span)[span_31](end_span).
* **Sample Input:** Dataset of 5 students, user selects "Sort by Marks" for a performance report.
* **Sample Output:** "Fastest: Merge Sort (Faster by 0.000008s)".

### Program 8: Search Engine Simulator
* **Aim:** Compare Binary Search against Hash Tables (Separate Chaining and Linear Probing) for word lookup[span_32](start_span)[span_32](end_span)[span_33](start_span)[span_33](end_span).
* **Logic:** Populates data mapped to IDs. Tracks internal comparison/probe counts during a search query[span_34](start_span)[span_34](end_span).
* **Sample Input:** Search word `word15`.
* **Sample Output:** Binary Search (5 comparisons), Chaining (1 probe), Probing (1 probe).

## Section F: Analysis

**1. Performance on Already-Sorted vs Random Input**
Quick sort performed noticeably worse on already-sorted input[span_35](start_span)[span_35](end_span). Merge sort stayed roughly the same regardless of input type[span_36](start_span)[span_36](end_span). Merge sort always mechanically halves the array, guaranteeing an $O(n \log n)$ structure. Quick sort (using the last-element pivot) failed to split already-sorted arrays, isolating only one element per recursive call, degrading to an explosive $O(n^2)$ time[span_37](start_span)[span_37](end_span).

**2. Basic Sorts on Reverse-Sorted Input**
Bubble sort was the slowest, requiring the absolute maximum possible number of comparisons and swaps[span_38](start_span)[span_38](end_span). Selection sort was the fastest of the three because, although it makes the same $O(n^2)$ comparisons, it only makes exactly $O(n)$ swaps, heavily reducing memory write operations[span_39](start_span)[span_39](end_span). This aligns perfectly with their theoretical worst-case mechanics.

**3. Divide and Conquer Discrepancy**
The performance difference between Merge and Quick sort on sorted data is entirely dictated by Quick sort's pivot choice[span_40](start_span)[span_40](end_span). Because our Quick sort explicitly picked the *last element* as the pivot[span_41](start_span)[span_41](end_span), a pre-sorted array means the pivot is always the absolute largest element, resulting in zero items in the right partition and $n-1$ items in the left, breaking the divide-and-conquer efficiency entirely[span_42](start_span)[span_42](end_span).

**4. Radix Sort Capabilities**
Radix sort performed incredibly fast compared to comparison-based algorithms because it maps digits directly rather than evaluating `<` or `>` between elements[span_43](start_span)[span_43](end_span). However, its usefulness is severely limited if the data is not comprised of uniform integers (like strings or floats without mapping), or if the integer range is massively huge (e.g., millions), which would require impractically large counting arrays and iteration passes[span_44](start_span)[span_44](end_span).

**5. Lookup Step Comparisons**
Both Hash Table versions required the fewest steps (averaging 1 probe)[span_45](start_span)[span_45](end_span). Binary search required significantly more steps (e.g., 5 comparisons)[span_46](start_span)[span_46](end_span). This perfectly validates their theoretical time complexities: Hashing provides expected $O(1)$ constant time lookup via direct index mapping, while Binary Search relies on $O(\log n)$ division[span_47](start_span)[span_47](end_span).

**6. Separate Chaining vs Linear Probing**
Separate Chaining handled collisions far better for our dataset because colliding keys were cleanly appended to a localized list[span_48](start_span)[span_48](end_span). If the hash table were 90 percent occupied, Linear Probing would suffer drastically from *primary clustering*—where long blocks of occupied slots force the algorithm to sequentially check many indexes, spiking lookup times exponentially[span_49](start_span)[span_49](end_span). Chaining isolates the problem strictly to the colliding index, maintaining better performance under heavy load[span_50](start_span)[span_50](end_span).
