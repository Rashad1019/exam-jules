def fibonacci(n):
    """Generate a Fibonacci sequence up to n elements."""
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

if __name__ == "__main__":
    n = 10
    print(f"The first {n} numbers in the Fibonacci sequence are: {fibonacci(n)}")
