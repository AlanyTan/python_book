list_1 = ['one', 'two', 'three']
range_1 = range(3)
dict_1 = dict(zip(list_1,range_1))
value_1, value_2, value_3 = dict_1.values()
print(f"# {value_1=},{value_2=},{value_3=}.")
# value_1=0,value_2=1,value_3=2.

value_1, *rest = dict_1.values()
print(f"# {value_1=}, {rest=}")
# value_1=0, rest=[1, 2]
