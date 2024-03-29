list_1 = ['one', 'two', 'three']
range_1 = range(3)
print(zip(list_1, range_1))
dict_1 = dict(zip(list_1, range_1))
print(f"# {dict_1=}")
# dict_1={'one': 0, 'two': 1, 'three': 2}

dict_2 = dict(enumerate(list_1))
print(f"# {dict_2=}")
# dict_2={0: 'one', 1: 'two', 2: 'three'}
