tuple_1 = (1, "2", 3.0)
tuple_2 = "Four", 5
print(f"# {tuple_1 + tuple_2=}")
# tuple_1 + tuple_2=(1, '2', 3.0, 'Four', 5)

print(f"# {tuple_2 * 3=}")
# tuple_2 * 3=('Four', 5, 'Four', 5, 'Four', 5)

tuple_1_alias = tuple_1
tuple_1 += tuple_2
print(f"# {tuple_1=}, {tuple_1_alias=}")
# tuple_1=(1, '2', 3.0, 'Four', 5), tuple_1_alias=(1, '2', 3.0)

tuple_2_alias = tuple_2
tuple_2 *= 2
print(f"# {tuple_2=}, {tuple_2_alias=}")
# tuple_2=('Four', 5, 'Four', 5), tuple_2_alias=('Four', 5)
