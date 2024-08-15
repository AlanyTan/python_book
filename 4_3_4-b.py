def fibonacci_iterative(n: int) -> int:
    """Calculates the nth Fibonacci number using an iterative approach.

    Args:
        n: The index of the Fibonacci number to calculate.

    Returns:
        The nth Fibonacci number.
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


print(f"# {fibonacci_iterative(10000)=}")
# fibonacci_iterative(10)=55
