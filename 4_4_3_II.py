def greet(desc: str, name: str = "World", seq: int = None) -> None:
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
        print(f"# lost track: Hello, {name}! ({desc})")
    else:
        print(f"# {seq:d} call: Hello, {name}! ({desc})")


greet(seq=1, name="John", desc="all args")
# 1 call: Hello, John! (all args)

greet("1 positional optional args", 2)
# lost track: Hello, 2! (1 positional optional args)

greet("1 named optional args", seq=2)
# 2 call: Hello, World! (1 named optional args)
