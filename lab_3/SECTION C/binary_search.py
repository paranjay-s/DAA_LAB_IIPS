def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    user_input = input("Enter SORTED numbers separated by space: ")
    arr = [int(x) for x in user_input.split()]
    target_exist = int(input("Enter a target that exists: "))
    target_missing = int(input("Enter a target that does not exist: "))
    
    print(f"Index of {target_exist}: {binary_search_iterative(arr, target_exist)}")
    print(f"Index of {target_missing}: {binary_search_iterative(arr, target_missing)}")
  
