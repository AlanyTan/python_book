print(f"# {any(range(10))=}, {all(range(10))=}")
# any(range(10))=True, all(range(10))=False

print(f"# {any([0, '', (), set(), {}, None, False])=}")
# any([0, '', (), set(), {}, None, False])=False

print(f"# {all((1, '1', (1), set('1'), {1: 1}, not None, True))=}")
# all((1, '1', (1), set('1'), {1:1}, not None, True))=True

tuple_1 = 1, 2, 3, 'A', 'B', 'C'
print(f"# {any([(x == 'A') for x in tuple_1])=}")
# any([(x == 'A') for x in tuple_1])=True

print(f"# {all([str(x) <= 'Z' for x in tuple_1])=}")
# all([str(x) <= 'Z' for x in tuple_1])=True

set_1 = {(1, 2, 3), '2', '3', '4'}
set_2 = {len(x) > 2 for x in set_1}
print(f"# {any(set_2)=}")
# any(set_2)=True

dict_1 = {k + 1: k for k in range(10)}
print(f"# {all(dict_1)=}")
# all(dict_1)=True
