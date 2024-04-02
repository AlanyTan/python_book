def func_demo_args(a, b=None, c: int = 1, /, d: int = 4, *, e=None, f):
    """This function demonstrates the usage of different types of 
    function arguments in Python.

    Args:
        a (any): A mandatory positional argument.
        b (Optional): An optional positional argument. 
            If provided, the value of `c` must also be provided.
        c: An optional positional argument. Default value is 1. 
            Can only be provied if `b` is provided.
        d: A mandatory keyword-only argument.
        e (Optional): An optional keyword-only argument. 
            If provided, the value of `d` must also be provided.
        f (any): A mandatory keyword-only argument.

    Returns:
        None
    """
    print(f"# Mandatory args: {a=}, {f=}")
    if b is None:
        print(f"# since b is ommitted, c must be ommitted as well.")
    else:
        print(f"# positional optional args: {b=}, {c=}")
    if e is None:
        print(f"# {d=}, and named parameter e is ommitted")
    else:
        print(f"# mamed optional arg: {d=}, {e=}")

func_demo_args('A', f='F')
# Mandatory args: a='A', f='F'
# since b is ommitted, c must be ommitted as well.
# d=4, and named parameter e is ommitted


func_demo_args('A', 'B', 3, 4, f='F')
# Mandatory args: a='A', f='F'
# positional optional args: b='B', c=3
# d=4, and named parameter e is ommitted

func_demo_args('A', f='F', d=4, e='E')
# Mandatory args: a='A', f='F'
# since b is ommitted, c must be ommitted as well.
# mamed optional arg: d=4, e='E'
