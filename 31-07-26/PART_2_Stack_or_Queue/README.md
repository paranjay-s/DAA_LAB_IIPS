# Part 2: Stack or Queue

* **Stack Execution Order:** Task5, Task4, Task3, Task2, Task1
* **Queue Execution Order:** Task1, Task2, Task3, Task4, Task5
* **Printer Strategy:** Queue (FIFO). Printers process jobs chronologically to ensure fairness. Print order: Task1 to Task5.

### Technical Implementation & Facts
* **Stack (LIFO):** Implemented using a standard Python `list`. `append()` and `pop()` operations at the end of a list take $O(1)$ constant time.
* **Queue (FIFO):** Implemented using `collections.deque` (Double-Ended Queue). 
* **Why not use a standard list for Queues?** Removing the first element `pop(0)` from a standard array is an $O(n)$ operation because memory must shift all remaining elements left. `deque.popleft()` is strictly $O(1)$.

### Acceptance Criteria Answers
* **Input:** A sequential array of strings: `["Task1", "Task2", "Task3", "Task4", "Task5"]`.
* **Output:** The LIFO processing array and the FIFO processing array.
* **Data Structure used:** Array (for Stack), Doubly Linked List / Deque (for Queue).
* **If input size grew 100 times:** Effort grows **proportionally** ($O(n)$). Processing 100x more tasks takes exactly 100x more time. The effort does not explode because every individual insert/remove operation runs in $O(1)$ constant time.