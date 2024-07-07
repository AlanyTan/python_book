list_of_tuple_0 = [(x, x*x) for x in range(6) if x % 2]
print(f"# {list_of_tuple_0=}")
# list_of_tuple_0=[(1, 1), (3, 9), (5, 25)]

list_1 = ['one', 'two', 'three']
dict_1 = {x: list_1[x] for x in range(3)}

dict_2 = dict_1.copy()

dict_1.update(list_of_tuple_0)
dict_2 |= list_of_tuple_0

print(f"# {dict_1 == dict_2=}, {dict_1=}")
# dict_1 == dict_2=True, dict_1={0: 'one', 1: 1, 2: 'three', 3: 9, 5: 25}

dict_2.clear()
print(f"# {dict_2=}")
# dict_2={}

print(f"# {dict_1.setdefault(4,'FOUR')=},\n# -{dict_1=}")
# dict_1.setdefault(4,'FOUR')='FOUR',
# -dict_1={0: 'one', 1: 1, 2: 'three', 3: 9, 5: 25, 4: 'FOUR'}

print(f"# {dict_1.pop(5)=},\n# -{dict_1=}")
# dict_1.pop(5)=25,
# -dict_1={0: 'one', 1: 1, 2: 'three', 3: 9, 4: 'FOUR'}

print(f"# {dict_1.popitem()=},\n# -{dict_1=}")
# dict_1.popitem()=(4, 'FOUR'),
# -dict_1={0: 'one', 1: 1, 2: 'three', 3: 9}
