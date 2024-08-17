list_1 = ['one', 'two', 'three']
dict_1_alias = dict_1 = dict(zip(list_1, range(3)))
print(f"# {dict_1=}")
# dict_1={'one': 0, 'two': 1, 'three': 2}

dict_1['three'] = 'II'
print(f"# {dict_1=}, {dict_1_alias is dict_1=}")
# dict_1={'one': 0, 'two': 1, 'three': 'II'}, dict_1_alias is dict_1=True

dict_1['four'] = 3
print(f"# {dict_1=}, {dict_1_alias is dict_1=}")
# dict_1={'one': 0, 'two': 1, 'three': 'II', 'four': 3}, dict_1_alias is dict_1=True

list_2 = [0, 1]
dict_1['two'] = list_2
print(f"# {dict_1=}, {dict_1['two'] is list_2=}")
# dict_1={'one': 0, 'two': [0, 1], 'three': 'II', 'four': 3}, dict_1['two'] is list_2=True

dict_1['four'] = list_2
print(f"# {dict_1=}, {dict_1['two'] is dict_1['four']=}")
# dict_1={'one': 0, 'two': [0, 1], 'three': 'II', 'four': [0, 1]}, dict_1['two'] is dict_1['four']=True

list_2.append(9)
print(f"# {dict_1=}, {dict_1_alias is dict_1=}")
# dict_1={'one': 0, 'two': [0, 1, 9], 'three': 'II', 'four': [0, 1, 9]}, dict_1_alias is dict_1=True
