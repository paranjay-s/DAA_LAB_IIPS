# 1D array operations: insert, delete, linear search, and left/right rotation.

def display_array(arr):
    print("Current array:", arr)

def insert_element(arr, index, value):
    if index < 0 or index > len(arr):
        print(f"Error: Index {index} is out of bounds (valid range: 0 to {len(arr)}).")
        return False
    arr.insert(index, value)
    print(f"Inserted {value} at index {index}.")
    display_array(arr)
    return True

def delete_element(arr, index):
    if len(arr) == 0:
        print("Error: Array is empty, cannot delete.")
        return False
    if index < 0 or index >= len(arr):
        print(f"Error: Index {index} is out of bounds (valid range: 0 to {len(arr) - 1}).")
        return False
    removed = arr.pop(index)
    print(f"Deleted value {removed} from index {index}.")
    display_array(arr)
    return True

def linear_search(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            print(f"Value {value} found at index {i}.")
            return i
    print(f"Value {value} was not found in the array.")
    return -1

def rotate_left(arr, k):
    n = len(arr)
    if n <= 1:
        print("Array has 0 or 1 element, rotation leaves it unchanged.")
        display_array(arr)
        return
    k = k % n
    arr[:] = arr[k:] + arr[:k]
    print(f"Rotated array left by {k} position(s).")
    display_array(arr)

def rotate_right(arr, k):
    n = len(arr)
    if n <= 1:
        print("Array has 0 or 1 element, rotation leaves it unchanged.")
        display_array(arr)
        return
    k = k % n
    arr[:] = arr[n - k:] + arr[:n - k]
    print(f"Rotated array right by {k} position(s).")
    display_array(arr)

def main():
    raw = input("Enter initial array elements separated by spaces (leave empty for empty array): ").strip()
    if raw:
        arr = [int(x) for x in raw.split()]
    else:
        arr = []

    display_array(arr)

    while True:
        print("\n--- 1D Array Menu ---")
        print("1. Insert value at index")
        print("2. Delete value at index")
        print("3. Linear search")
        print("4. Rotate left by k positions")
        print("5. Rotate right by k positions")
        print("6. Display array")
        print("7. Exit")

        choice = input("Enter choice (1-7): ").strip()

        if choice == '1':
            try:
                idx = int(input("Enter index to insert at: ").strip())
                val = int(input("Enter integer value to insert: ").strip())
                insert_element(arr, idx, val)
            except ValueError:
                print("Invalid input. Please enter integers.")

        elif choice == '2':
            try:
                idx = int(input("Enter index to delete: ").strip())
                delete_element(arr, idx)
            except ValueError:
                print("Invalid input. Please enter integers.")

        elif choice == '3':
            try:
                val = int(input("Enter value to search for: ").strip())
                linear_search(arr, val)
            except ValueError:
                print("Invalid input. Please enter integers.")

        elif choice == '4':
            try:
                k = int(input("Enter k (positions to rotate left): ").strip())
                if k < 0:
                    print("Please enter a non-negative integer.")
                else:
                    rotate_left(arr, k)
            except ValueError:
                print("Invalid input. Please enter integers.")

        elif choice == '5':
            try:
                k = int(input("Enter k (positions to rotate right): ").strip())
                if k < 0:
                    print("Please enter a non-negative integer.")
                else:
                    rotate_right(arr, k)
            except ValueError:
                print("Invalid input. Please enter integers.")

        elif choice == '6':
            display_array(arr)

        elif choice == '7':
            print("Exiting program.")
            break

        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
