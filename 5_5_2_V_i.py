range_1 = range(3)
set_1 = set(range_1)
print(f"# {set_1 == set_1.copy()=}, {set_1 is set_1.copy()=}")
# set_1 == set_1.copy()=True, set_1 is set_1.copy()=False

print(f"# {set_1.union([2, 0, 'a', 'b'])=}")
# set_1.union([2, 0, 'a', 'b'])={0, 1, 2, 'a', 'b'}

print(f"# {set_1.intersection([2, 0, 'a', 'b'])=}")
# set_1.intersection([2, 0, 'a', 'b'])={0, 2}

print(f"# {set_1.difference([2, 0, 'a', 'b'])=}")
# set_1.difference([2, 0, 'a', 'b'])={1}

print(f"# {set([2, 0, 'a', 'b']).difference(set_1)=}")
# set([2, 0, 'a', 'b']).difference(set_1)={'b', 'a'}

print(f"# {set_1.symmetric_difference([2, 0, 'a', 'b'])=}")
# set_1.symmetric_difference([2, 0, 'a', 'b'])={1, 'b', 'a'}

print(f"# {set_1.isdisjoint('123')=}")
# set_1.isdisjoint('123')=True

print(f"# {set_1.issuperset(range_1)=}")
# set_1.issuperset(range_1)=True

print(f"# {set_1.issubset(range(9))=}")
# set_1.issubset(range(9))=True
