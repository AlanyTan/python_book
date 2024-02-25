def greet(desc: str, name: str = "World", seq: int = None) -> None:
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
