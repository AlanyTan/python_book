list_1 = [1, "2", 3.0]
list_2 = [1, "4", 3.0]
list_2_copy = list_2.copy()

print(f"# {list_1 == list_2=}, {list_1 < list_2=}")
# list_1 == list_2=False, list_1 < list_2=True

print(f"# {list_2 == list_2_copy=}, {list_2 is list_2_copy=}")
# list_2 == list_2_copy=True, list_2 is list_2_copy=False

print(f"# {list_2 + [0] < list_2=}, {list_2 < [*list_2, 0]=}")
# list_2 + [0] < list_2=False, list_2 < [*list_2, 0]=True

print(f" #{list_2 in list_2 + [0]=}, {list_2 in [list_2, 0]}")
# list_2 in list_2 + [0]=False, True
