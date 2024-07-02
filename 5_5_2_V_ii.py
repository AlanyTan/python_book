range_1 = range(3)
set_1 = set(range_1)
print(f"# {set_1.add('abc')=}, {set_1=}")
# set_1.add('abc')=None, set_1={0, 1, 2, 'abc'}

print(f"# {set_1.update('abcd')=}, {set_1=}")
# set_1.update('abcd')=None, set_1={0, 1, 2, 'a', 'abc', 'd', 'b', 'c'}

print(f"# {set_1.remove('abc')=}, {set_1=}")
# set_1.remove('abc')=None, set_1={0, 1, 2, 'a', 'd', 'b', 'c'}

print(f"# {set_1.intersection_update([0, 2, 'a', 'c'])=}, {set_1=}")
# set_1.intersection_update([0, 2, 'a', 'c'])=None, set_1={0, 2, 'a', 'c'}

print(f"# {set_1.difference_update('abc')=}, {set_1=}")
# set_1.difference_update('abc')=None, set_1={0, 2}

print(f"# {set_1.symmetric_difference_update([2,'a'])=}, {set_1=}")
# set_1.symmetric_difference_update([2,'a'])=None, set_1={0, 'a'}
