def solve_part_1():
    # input list of numbers
    numbers = [8, 3, 15, 6, 2]
    
    # TASK 1: Find the biggest number
    biggest_so_far = numbers[0]
    comparisons_made = 0
    
    # Look at every number after the first one
    for current_number in numbers[1:]:
        comparisons_made += 1
        
        # If we find a bigger number, update our record
        if current_number > biggest_so_far:
            biggest_so_far = current_number
            
    print(f"The largest number is {biggest_so_far}.")
    print(f"It took {comparisons_made} comparisons to figure that out.")
    
    # TASK 2: Sort the numbers 
    organized_numbers = sorted(numbers)
    
    print(f"Here is the sorted list: {organized_numbers}")

# Run the function
solve_part_1()