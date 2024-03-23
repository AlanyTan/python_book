list_alias = list_example = [1,2,"3","four",5.0, 'placeholder']
print(f"#  original  {list_example}")
#  original  [1, 2, '3', 'four', 5.0, 'placeholder']

list_example[0] = "10"
print(f"# {list_alias=}")
# list_alias=['10', 2, '3', 'four', 5.0, 'placeholder']

list_example[-1] = ['a', 'b']
print(f"# {list_alias=}")
# list_alias=['10', 2, '3', 'four', 5.0, ['a', 'b']]

list_example[1:3]=["two & III"]
print(f"# {list_alias=}")
# list_alias=['10', 'two & III', 'four', 5.0, ['a', 'b']]

list_example[len(list_example):len(list_example)]=['additional', 'items']
print(f"# {list_alias=}")
# list_alias=['10', 'two & III', 'four', 5.0, ['a', 'b'], 'additional', 'items']

list_alias[1:6:2]=['B','D','F']
print(f"# {list_example=}")
# list_alias=['10', 'B', 'four', 'D', ['a', 'b'], 'F', 'items']

list_alias[4:]=[]
print(f"# {list_example=}") 
# list_alias=['10', 'B', 'four', 'D']
