print(f"# {len('abcdefghijklmnopqrstuvwxyz')=}")
# len('abcdefghijklmnopqrstuvwxyz')=26

print(f"# {len(range(10))=}")
# len(range(10))=10

print(f"# {len([x for x in range(100) if not (x % 2 + x % 3)])=}")
# len([x for x in range(100) if not (x%2 + x%3)])=17

print(f"# {len({x**2 for x in range(-100, 101)})=}")
# len({x**2 for x in range(-100,101)})=101

print(f"# {len(dict([('one', 0), ('two', 1)], two=1, three=2))=}")
# len(dict([('one',0), ('two', 1)], two=1, three=2))=3
