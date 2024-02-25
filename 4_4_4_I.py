def greet(description: str, name: str = "World", seq: int = None, *, onemore) -> None:
    if seq is None:
        print(f"# lost track: Hello, {name}! (called {description})")
    else:
        print(f"# {seq:d} call: Hello, {name}! (called {description})")


greet("with optional argument", "John", 1)
# 1 call: Hello, John! (called with optional argument)

greet("without optional argument")
# lost track: Hello, World! (called without optional argument)
