def bubble_sort(arr):
    n = len(arr)
    arr_copy = arr.copy()
    print("\n--- Bubble Sort Steps ---")
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
        print(f"Pass {i+1}: {arr_copy}")
        if not swapped:
            break
    return arr_copy

def selection_sort(arr):
    n = len(arr)
    arr_copy = arr.copy()
    print("\n--- Selection Sort Steps ---")
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr_copy[min_idx] > arr_copy[j]:
                min_idx = j
        arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]
        print(f"Step {i+1}: {arr_copy}")
    return arr_copy

def insertion_sort(arr):
    arr_copy = arr.copy()
    print("\n--- Insertion Sort Steps ---")
    for i in range(1, len(arr_copy)):
        key = arr_copy[i]
        j = i - 1
        while j >= 0 and key < arr_copy[j]:
            arr_copy[j + 1] = arr_copy[j]
            j -= 1
        arr_copy[j + 1] = key
        print(f"Inserted {key}: {arr_copy}")
    return arr_copy

if __name__ == "__main__":
    user_input = input("Enter numbers separated by space: ")
    arr = [int(x) for x in user_input.split()]
    bubble_sort(arr)
    selection_sort(arr)
    insertion_sort(arr)
  
