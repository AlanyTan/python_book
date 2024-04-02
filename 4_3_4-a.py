def fibonacci(n) -> int:
    """Calculates the nth Fibonacci number.

    Args:
        n (int): The index of the Fibonacci number to calculate.

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(f"# {fibonacci(10)=}")
# fibonacci(10)=55
