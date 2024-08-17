list_1 = ['one', 'two', 'three']
range_1 = range(3)
dict_1 = dict(zip(list_1, range_1))
print(f"# {dict_1.get('one')=}")
# dict_1['one']=0

dict_1[4] = [0, 1, 2, 3]
print(f"# {dict_1.get(4)=}")
# dict_1.get(4)=[0, 1, 2, 3]

print(f"# {dict_1.get(5)=}")
# dict_1.get(5)=None
