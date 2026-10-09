## Part 1: Trace It Yourself 

1. Finding the Largest Number
We assume the first number (8) is the largest, then check the rest one by one:

3 > 8? No.

15 > 8? Yes! (New largest is 15)

6 > 15? No.

2 > 15? No.
Result: 15. We made 4 comparisons to find it.

2. Sorting the List (The Efficient Way)
While a human might sort by repeatedly looking for the smallest number, our code uses Python's built-in sorted() function. Python uses Timsort. This is a "divide and conquer" algorithm that slices the list into tiny pieces, sorts them, and efficiently merges them back together.


# Acceptance Criteria

1. Input: The list [8, 3, 15, 6, 2].

2. Output: Largest number (15), comparisons made (4), and sorted list [2, 3, 6, 8, 15].

3. Data Structure: An Array (known as a List in Python).

4. If input grew 100 times: 
Finding the largest number grows proportionally (100x more numbers = 100x more comparisons). Sorting using Timsort grows a bit faster than proportionally, but it successfully avoids the "explosive" growth of basic manual sorting methods, making it perfectly suited for large-scale data.

