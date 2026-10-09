def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L, R = arr[:mid], arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k], i = L[i], i + 1
            else:
                arr[k], j = R[j], j + 1
            k += 1
        while i < len(L):
            arr[k], i, k = L[i], i + 1, k + 1
        while j < len(R):
            arr[k], j, k = R[j], j + 1, k + 1
    return arr

# Quick sort using the LAST element as the pivot strategy
def quick_sort(arr, low, high):
    if low < high:
        pivot = arr[high] # Strategy: Last element as pivot
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pi = i + 1
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr

def heapify(arr, n, i):
    largest = i
    l, r = 2 * i + 1, 2 * i + 2
    if l < n and arr[l] > arr[largest]: largest = l
    if r < n and arr[r] > arr[largest]: largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

if __name__ == "__main__":
    user_input = input("Enter numbers separated by space: ")
    arr = [int(x) for x in user_input.split()]
    print("Merge Sort:", merge_sort(arr.copy()))
    print("Quick Sort:", quick_sort(arr.copy(), 0, len(arr) - 1))
    print("Heap Sort:", heap_sort(arr.copy()))
  
