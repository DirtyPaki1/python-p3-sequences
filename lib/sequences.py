#!/usr/bin/env python3

# sequences.py

def print_fibonacci(n):
    """
    Prints the Fibonacci sequence up to the nth term.
    
    Parameters:
    - n: int, the length of the Fibonacci sequence to print.
    """
    # Initialize the first two Fibonacci numbers
    fib_numbers = [0, 1]
    
    # Generate the rest of the Fibonacci sequence up to n terms
    for _ in range(2, n):
        next_number = fib_numbers[-1] + fib_numbers[-2]
        fib_numbers.append(next_number)
    
    # Print the Fibonacci numbers in the required format, up to the nth term
    print(f"[{', '.join(map(str, fib_numbers[:n]))}]")



