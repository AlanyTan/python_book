print(f"# {any(range(10))=}, {all(range(10))=}")
# any(range(10))=True, all(range(10))=False

print(f"# {any([0, '', (), set(), {}, None, False])=}")
# any([0, '', (), set(), {}, None, False])=False

print(f"# {all((1, '1', (1), set('1'), {1:1}, not None, True))=}")
# all((1, '1', (1), set('1'), {1:1}, not None, True))=True
