list_1 = ['one', 'two', 'three']
range_1 = range(3)
dict_1 = dict(zip(list_1, range_1))
print(f"# {dict_1['one']=}")
# dict_1['one']=0

dict_1[4] = [0, 1, 2, 3]
print(f"# {dict_1=}")
# dict_1={'one': 0, 'two': 1, 'three': 2, 4: [0, 1, 2, 3]}
