def greet(description: str, name: str = "World", seq: int = None) -> None:
    """The function prints a greeting message based on the provided parameters.

    Args:
        description: required description of how the function was called.
        name: the name of the person to greet, if omitted, will use value 'World'.
        seq: the sequence number of the time greeted, if omitted, will print
            'lost tract' as the start of the greeting
    
    Returns:
        None.
    """
    if seq is None:
        print(f"# lost track: Hello, {name}! (called {description})")
    else:
        print(f"# #{seq:d} call: Hello, {name}! (called {description})")


greet("with optional argument", "John", 1)
# #1 call: Hello, John! (called with optional argument)

greet("without optional argument")
# lost track: Hello, World! (called without optional argument)
