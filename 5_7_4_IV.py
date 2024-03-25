dict_0 = {x: x*x for x in range(-5, 6) if x % 2}
print(f"# {dict_0=}")
# dict_0={-5: 25, -3: 9, -1: 1, 1: 1, 3: 9, 5: 25}

list_1 = ['one', 'two', 'three']
range_1 = range(3)

dict_1 = {list_1[x]: x for x in range_1}
print(f"# {dict_1=}")
# dict_1={'one': 0, 'two': 1, 'three': 2}


dict_1_flip = {value: key for key, value in dict_1.items()}
print(f"# {dict_1_flip=}")
# dict_1_flip={0: 'one', 1: 'two', 2: 'three'}
