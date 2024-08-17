str_1 = "ABC"
print("# the string str_1 is", str_1, sep=', ')
# the string str_1 is, ABC

print("# unpacked str_1 are", *str_1, sep=', ')
# unpacked str_1 are, A, B, C


def func_demo_unpacking(arg1: str, arg2: str, arg3: str) -> None:
    """demonstraing unpacking a str to 3 chars
    """
    print(f"#  func_demo_unpacking received {arg1=}, {arg2=}, {arg3=}")


func_demo_unpacking(*str_1[:2], arg3='z')
#  func_demo_unpacking received arg1='A', arg2='B', arg3='z'
