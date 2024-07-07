list_1 = ['one', 'two', 'three']
dict_1 = dict(zip(list_1,range(3)))
dict_2 = dict(zip(list_1,range(3)))

print(f"#  {dict_1 is dict_2=}")
#  dict_1 is dict_2=False

print(f"#  {dict_1 == dict_2=}")
#  dict_1 == dict_2=True

dict_1['one'] = 'zero'
print(f"#  {dict_1 == dict_2=}")
#  dict_1 == dict_2=False
