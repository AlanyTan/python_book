def func_demo_args(a, b=None, c: int = 1, /, d: int = 4, *, e=None, f) -> None:
    """This function demonstrates the usage of different types of 
    function arguments in Python.

    Args:
        a: required positional only argument.
        b: optional positional only argument. 
            If omitted, c has to be ommitted as well.
        c: optional positional argument. Default value is 1. 
            Can only be provied if `b` is provided.
        d: required positional or keyword argument.
        e: optional keyword-only argument. 
            if provided have to be after a, b, c, d.
        f: A required keyword-only argument.

    Returns:
        None
    """
    print(f"# Required args: {a=}, {f=}")
    if b is None:
        print(f"# since b is ommitted, c must be ommitted as well.")
    else:
        print(f"# positional optional args: {b=}, {c=}")
    if e is None:
        print(f"# {d=}, and named parameter e is ommitted")
    else:
        print(f"# mamed optional arg: {d=}, {e=}")


func_demo_args('A', f='F')
# Required args: a='A', f='F'
# since b is ommitted, c must be ommitted as well.
# d=4, and named parameter e is ommitted

func_demo_args('A', 'B', 3, 4, f='F')
# Required args: a='A', f='F'
# positional optional args: b='B', c=3
# d=4, and named parameter e is ommitted

func_demo_args('A', f='F', d=4, e='E')
# Required args: a='A', f='F'
# since b is ommitted, c must be ommitted as well.
# mamed optional arg: d=4, e='E'
