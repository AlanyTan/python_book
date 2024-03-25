list_1 = ['one', 'two', 'three']
dict_1 = dict(zip(list_1,range(3)))
dict_2 = dict(two='a', three='b', four='c')

print(f"#  {dict_1=},\n# -{dict_2=},\n# -{dict_1 | dict_2=}")
#  dict_1={'one': 0, 'two': 1, 'three': 2},
# -dict_2={'two': 'a', 'three': 'b', 'four': 'c'},
# -dict_1 | dict_2={'one': 0, 'two': 'a', 'three': 'b', 'four': 'c'}

dict_1_alias = dict_1
dict_1 |= dict_2
print(f"#  {dict_1=},\n# -{dict_2=}")
#  dict_1={'one': 0, 'two': 'a', 'three': 'b', 'four': 'c'},
# -dict_2={'two': 'a', 'three': 'b', 'four': 'c'}
print(f"#  {dict_1 is dict_1_alias=}")
#  dict_1 is dict_1_alias=True

dict_1 = dict(zip(list_1,range(3)))
dict_2 |= dict_1
print(f"#  {dict_1=},\n# -{dict_2=}")
#  dict_1={'one': 0, 'two': 'a', 'three': 'b', 'four': 'c'},
# -dict_2={'two': 'a', 'three': 'b', 'four': 'c', 'one': 0}
