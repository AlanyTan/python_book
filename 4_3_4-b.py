def fibonacci_iterative(n) -> int:
    """Calculates the nth Fibonacci number using an iterative approach.

    Args:
        n (int): The index of the Fibonacci number to calculate.

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 1:
        return n
    a = 0
    b = 1
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return b

print(f"# {fibonacci_iterative(n=10)=}")
# fibonacci_iterative(10)=55
