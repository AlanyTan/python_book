list_1 = ['one', 'two', 'three']
range_1 = range(3)
dict_1 = dict.fromkeys(list_1)
print(f"# {dict_1=}")
# dict_1={'one': None, 'two': None, 'three': None}

dict_2 = dict.fromkeys(list_1, range_1)
print(f"# {dict_2=}")
# dict_2={'one': range(0, 3), 'two': range(0, 3), 'three': range(0, 3)}
