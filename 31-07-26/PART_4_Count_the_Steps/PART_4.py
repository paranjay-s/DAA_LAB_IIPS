def solve_part_4():
    # Single Loop
    # FOR i = 1 to 5
    count_1 = sum(1 for i in range(1, 6))
    print(f"Single loop (n=5) runs: {count_1} times")
    
    # FOR i = 1 to 20
    count_2 = sum(1 for i in range(1, 21))
    print(f"Single loop (n=20) runs: {count_2} times")
    
    # Nested Loops
    # FOR i = 1 to 5, FOR j = 1 to 5
    count_3 = sum(1 for i in range(1, 6) for j in range(1, 6))
    print(f"Nested loop inner PRINT (n=5) runs: {count_3} times")
    
    # Both loops 1 to 10
    count_4 = sum(1 for i in range(1, 11) for j in range(1, 11))
    print(f"Nested loop inner PRINT (n=10) runs: {count_4} times")

solve_part_4()