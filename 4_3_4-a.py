def fibonacci(n) -> int:
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(f"# {fibonacci(10)=}")
# fibonacci(10)=55
