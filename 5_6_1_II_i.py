dict_1 = dict(one=1, two=2, three=3)
print(f"# {dict_1=}")
# dict_1={'one': 1, 'two': 2, 'three': 3}

dict_2 = dict([(2, 'two'), (1, 'one'), ('three', 3), (1, 1)])
print(f"# {dict_2=}")
# dict_2={2: 'two', 1: 1, 'three': 3}

dict_3 = dict([[1, 'one'], [2, 'two'], ['three', 3]],  three='3.0', four='4') 
print(f"# {dict_3=}")
# dict_3={1: 'one', 2: 'two', 'three': '3.0', 'four': '4'}
