# Part 4: Count the Steps

* **Single Loop (1 to 5):** Runs 5 times.
* **Single Loop (1 to 20):** Runs 20 times.
* **Nested Loops (1 to 5):** Inner print runs 25 times ($5 \times 5$).
* **Nested Loops (1 to 10):** Inner print runs 100 times ($10 \times 10$).

### Technical Implementation & Facts
* **Single Loop Complexity:** $O(n)$ (Linear time). Executions scale exactly 1:1 with `n`.
* **Nested Loop Complexity:** $O(n^2)$ (Quadratic time). Every outer step triggers a full set of inner steps.
* **Calculation Rule:** Total steps = (outer loop limit) $\times$ (inner loop limit).

### Acceptance Criteria Answers
* **Input:** Integer boundary values defining the loop limits (`n=5`, `n=10`, `n=20`).
* **Output:** Total integer counts of loop executions (5, 20, 25, 100).
* **Data Structure used:** None. Only primitive integer variables and control flow mechanisms.
* **If input size grew 100 times:** 
  * Single loop effort grows **proportionally** ($100x$). 
  * Nested loop effort grows **explosively** ($100^2$ or $10,000x$). This proves why nested loops must be avoided when processing large datasets.