def fibonacci(n: int) -> int:
    """Calculates the nth Fibonacci number.

    Args:
        n: The index of the Fibonacci number to calculate.

    Returns:
        The nth Fibonacci number.
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(f"# {fibonacci(10)=}")
# fibonacci(10)=55
