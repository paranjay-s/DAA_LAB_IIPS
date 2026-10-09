import time
import random
import csv
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(10000)

# --- Sorting Algorithms ---
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped: break
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]: min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key, j = arr[i], i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1], j = arr[j], j - 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L, R = arr[:mid], arr[mid:]
        merge_sort(L); merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]: arr[k], i = L[i], i + 1
            else: arr[k], j = R[j], j + 1
            k += 1
        while i < len(L): arr[k], i, k = L[i], i + 1, k + 1
        while j < len(R): arr[k], j, k = R[j], j + 1, k + 1
    return arr

def quick_sort(arr, low=0, high=None):
    if high is None: high = len(arr) - 1
    if low < high:
        pivot = arr[high]
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
    largest, l, r = i, 2 * i + 1, 2 * i + 2
    if l < n and arr[l] > arr[largest]: largest = l
    if r < n and arr[r] > arr[largest]: largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1): heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

# --- Timing & Graphing Logic ---
def run_analysis():
    sizes = [100, 500, 1000, 2000]
    input_types = ["random", "sorted", "reverse"]
    algorithms = {
        "Bubble": bubble_sort, "Selection": selection_sort, "Insertion": insertion_sort,
        "Merge": merge_sort, "Quick": quick_sort, "Heap": heap_sort
    }
    
    results = []
    
    # 1. Generate Data & Time
    print(f"{'Algorithm':<12} | {'Input Type':<10} | {'N':<6} | {'Time (s)'}")
    print("-" * 45)
    
    for n in sizes:
        datasets = {
            "random": [random.randint(1, 10000) for _ in range(n)],
            "sorted": list(range(n)),
            "reverse": list(range(n, 0, -1))
        }
        
        for input_type, data in datasets.items():
            for algo_name, algo_func in algorithms.items():
                test_arr = data.copy()
                
                start_time = time.perf_counter()
                algo_func(test_arr)
                end_time = time.perf_counter()
                
                time_taken = end_time - start_time
                results.append((algo_name, input_type, n, time_taken))
                print(f"{algo_name:<12} | {input_type:<10} | {n:<6} | {time_taken:.6f}")

    # 2. Save CSV
    with open("timing_data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Algorithm", "Input Type", "N", "Time"])
        writer.writerows(results)
        
    # 3. Plot Graphs
    plt.figure(figsize=(10, 5))
    for algo in algorithms:
        algo_data = [r for r in results if r[0] == algo and r[1] == "random"]
        plt.plot([r[2] for r in algo_data], [r[3] for r in algo_data], marker='o', label=algo)
    plt.title("Algorithm Performance on Random Input")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.savefig("graph_random_input.png")
    
    plt.figure(figsize=(10, 5))
    for algo in algorithms:
        algo_data = [r for r in results if r[0] == algo and r[1] == "sorted"]
        plt.plot([r[2] for r in algo_data], [r[3] for r in algo_data], marker='o', label=algo)
    plt.title("Algorithm Performance on Sorted Input")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.savefig("graph_sorted_input.png")
    print("\nCSV and Graphs saved successfully in lab_3 folder.")

if __name__ == "__main__":
    run_analysis()
      
