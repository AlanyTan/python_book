def greet(description: str, name: str = "World", seq: int = None) -> None:
    """Prints a greeting message based on the provided arguments.

    Args:
        description: required description of how the function was called.
        name: optional the name of the person to greet, 
              if omitted, will use value 'World'.
        seq: optional the sequence number of the time greeted, 
             if omitted, will print 'lost tract' as the start of the greeting
    """
    if seq is None:
        print(f"# lost track: Hello, {name}! (called {description})")
    else:
        print(f"# #{seq:d} call: Hello, {name}! (called {description})")


greet("with optional arguments", "John", 1)
# #1 call: Hello, John! (called with optional argument)

greet("without optional argument")
# lost track: Hello, World! (called without optional argument)
