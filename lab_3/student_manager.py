import time

# Sorting algorithms adapted for dictionary keys
def bubble_sort(arr, key):
    n = len(arr)
    arr_copy = arr.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr_copy[j][key] > arr_copy[j + 1][key]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
    return arr_copy

def merge_sort(arr, key):
    if len(arr) > 1:
        mid = len(arr) // 2
        L, R = merge_sort(arr[:mid], key), merge_sort(arr[mid:], key)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i][key] < R[j][key]:
                arr[k], i = L[i], i + 1
            else:
                arr[k], j = R[j], j + 1
            k += 1
        while i < len(L): arr[k], i, k = L[i], i + 1, k + 1
        while j < len(R): arr[k], j, k = R[j], j + 1, k + 1
    return arr

def binary_search(arr, target_roll):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid]["roll"] == target_roll: return arr[mid]
        elif arr[mid]["roll"] < target_roll: low = mid + 1
        else: high = mid - 1
    return None

def performance_report(data, key):
    start = time.perf_counter()
    bubble_sort(data, key)
    bubble_time = time.perf_counter() - start
    
    start = time.perf_counter()
    merge_sort(data.copy(), key)
    merge_time = time.perf_counter() - start
    
    print("\n--- Performance Report ---")
    print(f"Bubble Sort Time: {bubble_time:.6f}s")
    print(f"Merge Sort Time:  {merge_time:.6f}s")
    if merge_time < bubble_time:
        print(f"Fastest: Merge Sort (Faster by {bubble_time - merge_time:.6f}s)")
    else:
        print(f"Fastest: Bubble Sort (Faster by {merge_time - bubble_time:.6f}s)")

if __name__ == "__main__":
    students = [
        {"roll": 105, "name": "Alice", "marks": 88},
        {"roll": 101, "name": "Bob", "marks": 92},
        {"roll": 103, "name": "Charlie", "marks": 75},
        {"roll": 104, "name": "David", "marks": 99},
        {"roll": 102, "name": "Eve", "marks": 81}
    ]
    
    print("1. Sort by Roll")
    print("2. Search by Roll (Requires Sort)")
    print("3. Performance Report (Sort by Marks)")
    choice = input("Enter choice: ")
    
    if choice == "1":
        print(merge_sort(students, "roll"))
    elif choice == "2":
        sorted_students = merge_sort(students, "roll")
        roll = int(input("Enter Roll to search: "))
        print("Found:", binary_search(sorted_students, roll))
    elif choice == "3":
        performance_report(students, "marks")
      
