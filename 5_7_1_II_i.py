dict_1 = dict(one=1, two=2, three=3)
print(f"# {dict_1=}")
# dict_1={'one': 1, 'two': 2, 'three': 3}

dict_2 = dict([('two', 2), ('one', 1), ('three', 3), ('one',"1")])
print(f"# {dict_2=}")
# dict_2={'two': 2, 'one': '1', 'three': 3}

dict_3 = dict([['one', 1], ['two', '2'], ['three', 3]],  two=2) 
print(f"# {dict_3=}")
# dict_3={'one': 1, 'two': 2, 'three': 3}
