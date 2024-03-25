list_1 = ['one', 'two', 'three']
range_1 = range(3)
dict_1 = dict(zip(list_1,range_1))

item_1, item_2, item_3 = dict_1.items()
print(f"# {item_1=}, {item_2=}, {item_3=}")
# item_1=('one', 0), item_2=('two', 1), item_3=('three', 2)

for key, value  in dict_1.items():
    print(f"# {key=}, {value=}")
# key='one', value=0
# key='two', value=1
# key='three', value=2
