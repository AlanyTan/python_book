def func_demo_args(a, b=None, c=1, /, d=4, *, e=None, f):
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


func_demo_args('A', 'B', 'C', 'D', f='F')
# Mandatory args: a='A', f='F'
# positional optional args: b='B', c='C'
# d='D', and named parameter e is ommitted

func_demo_args('A', f='F', d='D', e='E')
# Mandatory args: a='A', f='F'
# since b is ommitted, c must be ommitted as well.
# mamed optional arg: d=D, e='E'
