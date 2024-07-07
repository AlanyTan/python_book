list_1 = ['one', 'two', 'three']
dict_1 = dict(zip(list_1,range(3)))

print(f"#  {'one' in dict_1=}")
#  'one' in dict_1=True

print(f"#  {0 in dict_1=}")
#  0 in dict_1=False

print(f"#  {0 in dict_1.values()=}")
#  0 in dict_1.values()=True

print(f"#  {('one',0) in dict_1.items()=}")
#  ('one',0) in dict_1.items()=True
