# Theory Answers

## Section A: Concept Check
1. Bubble sort works by repeatedly swapping **adjacent** elements if they are in the wrong order[span_0](start_span)[span_0](end_span).
2. Selection sort repeatedly finds the **minimum** element from the unsorted part and places it at the beginning[span_1](start_span)[span_1](end_span).
3. Insertion sort builds the sorted portion one element at a time by **inserting** each new element into its correct position[span_2](start_span)[span_2](end_span).
4. Merge sort follows a **divide** and **conquer** approach: split the array, sort each half, then combine[span_3](start_span)[span_3](end_span).
5. Quick sort picks a **pivot** and partitions the array around it before recursing[span_4](start_span)[span_4](end_span).
6. Heap sort relies on a data structure called a **heap (max-heap/min-heap)** which is typically implemented using an array[span_5](start_span)[span_5](end_span).
7. Radix sort processes numbers digit by digit, starting from the **least** significant digit (in the standard LSD version)[span_6](start_span)[span_6](end_span).
8. Binary search requires the input array to be **sorted** before it can be used[span_7](start_span)[span_7](end_span).
9. In hashing, when two different keys map to the same index, this is called a **collision**[span_8](start_span)[span_8](end_span).
10. Separate chaining resolves collisions by storing multiple values at the same index using a **linked list**, while linear probing resolves them by **finding the next available (empty) slot**[span_9](start_span)[span_9](end_span).

## Section B: Trace the Logic
* **1. Bubble Sort [5, 2, 8, 1, 9] (Pass 1):** [2, 5, 8, 1, 9] $\rightarrow$ [2, 5, 8, 1, 9] $\rightarrow$ [2, 5, 1, 8, 9] $\rightarrow$ [2, 5, 1, 8, 9][span_10](start_span)[span_10](end_span).
* **2. Selection Sort [5, 2, 8, 1, 9]:** Swap 1 & 5: [1, 2, 8, 5, 9] $\rightarrow$ Swap 2 & 2: [1, 2, 8, 5, 9] $\rightarrow$ Swap 5 & 8: [1, 2, 5, 8, 9] $\rightarrow$ Swap 8 & 8: [1, 2, 5, 8, 9][span_11](start_span)[span_11](end_span).
* **3. Insertion Sort [5, 2, 8, 1, 9]:** Insert 2: [2, 5, 8, 1, 9] $\rightarrow$ Insert 8: [2, 5, 8, 1, 9] $\rightarrow$ Insert 1: [1, 2, 5, 8, 9] $\rightarrow$ Insert 9: [1, 2, 5, 8, 9][span_12](start_span)[span_12](end_span).
* **4. Merge Sort Splitting [8, 3, 5, 4, 7, 6, 1, 2]:** [8, 3, 5, 4], [7, 6, 1, 2] $\rightarrow$ [8, 3], [5, 4], [7, 6], [1, 2] $\rightarrow$ [8], [3], [5], [4], [7], [6], [1], [2][span_13](start_span)[span_13](end_span).
* **5. Quick Sort Partition [8, 3, 5, 4, 7, 6, 1, 2] (Pivot 2):** Array becomes [1, 2, 5, 4, 7, 6, 8, 3]. Pivot's final index is 1[span_14](start_span)[span_14](end_span).
* **6. Radix Sort [170, 45, 75, 90, 802, 24, 2, 66]:** 
  * Ones: [170, 90, 802, 2, 24, 45, 75, 66]
  * Tens: [802, 2, 24, 45, 66, 170, 75, 90][span_15](start_span)[span_15](end_span).
* **7. Binary Search for 23 on [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]:** low=0, high=10, mid=5. Value at mid is 23. Target found in 1 step[span_16](start_span)[span_16](end_span).
* **8. Hash Table (Separate Chaining):** Index 2: [9]. Index 3: [10 $\rightarrow$ 3 $\rightarrow$ 17 $\rightarrow$ 24][span_17](start_span)[span_17](end_span).
* **9. Hash Table (Linear Probing):** Index 2: 9. Index 3: 10. Index 4: 3. Index 5: 17. Index 6: 24[span_18](start_span)[span_18](end_span).

## Section F: Expected Analysis Outcomes
* **1. Sorted Input Performance:** Quick sort (with last-element pivot) performs worse (degrades to $O(n^2)$). Merge sort stays roughly the same ($O(n \log n)$) because it always divides arrays equally regardless of input order[span_19](start_span)[span_19](end_span).
* **2. Reverse-sorted Basic Sorts:** Bubble sort is typically slowest due to maximum required swaps ($O(n^2)$ worst case). Selection sort is often fastest of the three basic algorithms here because it only makes $O(n)$ swaps total, despite $O(n^2)$ comparisons[span_20](start_span)[span_20](end_span).
* **3. Divide & Conquer Differences:** Quick sort's performance drops on already-sorted input if the last element is chosen as the pivot, leading to completely unbalanced partitions. Merge sort guarantees perfectly balanced halves[span_21](start_span)[span_21](end_span).
* **4. Radix Sort Efficiency:** Very fast for integers ($O(nk)$), but heavily limited for strings, floats, or objects lacking clear positional properties, and highly inefficient if the range of values is massively larger than the dataset size[span_22](start_span)[span_22](end_span).
* **5. Lookup Comparisons:** Hash tables generally require fewer steps ($O(1)$ expected) compared to Binary Search ($O(\log n)$)[span_23](start_span)[span_23](end_span).
* **6. Collision Handling:** Separate Chaining handles collisions better for highly clustered data and remains effective even if the table is 90% full. Linear probing suffers heavily from primary clustering as the table fills up, causing probe lengths to spike exponentially[span_24](start_span)[span_24](end_span).
* 
