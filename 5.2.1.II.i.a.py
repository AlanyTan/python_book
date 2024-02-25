def func_demo_unpacking(arg1: str, arg2: str, arg3: str) -> None:
    print(f"# received {arg1=}, {arg2=}, {arg3=}")
    
str_1 = "abc"
print(f"# the string is: {str_1}")
# the string is: abc

func_demo_unpacking(*str_1)
# received arg1='a', arg2='b', arg3='c'
