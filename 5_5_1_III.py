string_example = "AbCdEfABCDEF"
tuple_example = (1, 2, "3", "four", 5.0, 1)

print(f"# convert string to: {set(string_example)}")
# convert string to: {'d', 'E', 'B', 'D', 'b', 'f', 'F', 'A', 'C'}

print(f"# convert tuple to: {set(tuple_example)}")
# convert tuple to: {1, 2, 5.0, 'four', '3'}

print(f"# convert range to: {frozenset(range(4))}")
# convert range to: frozenset({0, 1, 2, 3})

print(f"# convert filtered to: {frozenset(filter(lambda x: x <= 'Z',
                                                 string_example))}")
# convert set to: frozenset({'E', 'B', 'D', 'F', 'A', 'C'})
