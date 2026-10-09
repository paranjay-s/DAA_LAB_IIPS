from collections import deque

def solve_part_2():
    tasks = ["Task1", "Task2", "Task3", "Task4", "Task5"]
    
    # Stack Implementation (LIFO) 
    stack = []
    # Push tasks (O(1) time)
    for task in tasks:
        stack.append(task)
    
    stack_order = []
    # Pop tasks (O(1) time)
    while stack:
        stack_order.append(stack.pop())
        
    print(f"Stack Processing Order: {stack_order}")
    
    # Queue Implementation (FIFO)
    # Using deque instead of list because deque.popleft() is O(1), list.pop(0) is O(n)
    queue = deque(tasks)
    
    queue_order = []
    # Dequeue tasks (O(1) time)
    while queue:
        queue_order.append(queue.popleft())
        
    print(f"Queue Processing Order: {queue_order}")
    print(f"Printer Processing Order (Queue): {queue_order}")

solve_part_2()