list_1 = ['one', 'two', 'three']
dict_1 = dict(zip(list_1,range(3)))

def func_named_pars(three: int, two: int, one: int, four: int = 999) -> None:
    print(f"# inside func, received args: {one=}, {two=}, {three=}, {four=}")
# inside func, received args: one=0, two=1, three=2, four=999

func_named_pars(**dict_1)
