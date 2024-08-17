str_1 = "ABCDEF"
print(f"# {'ABC' in str_1=}")
# 'ABC' in str_1=True

list_1 = [1, 2, 3, 4, [5, 6]]
print(f"# {[5, 6] in list_1=}")
# [5, 6] in list_1=True

tuple_1 = ('a', 'b', 'c')
print(f"# {('a', 'b', 'c') not in tuple_1=}")
# ('a', 'b', 'c') not in tuple_1=True

set_1 = {'one', 'two', 'three'}
print(f"# {'one' in set_1=}")
# 'one' in set_1=True

dict_1 = dict(zip(tuple_1, set_1))
print(f"# {'a' not in dict_1=}")
# 'a' not in dict_1=False
