set_1 = {1, "2", 3.0}
set_2 = {"2", 1}
set_3 = {1, "4", 3.0}
set_4 = {1, "2", 1, "2"}

print(f"# {set_1 > set_2=}, {set_1 >= set_2=}, {set_1 <= set_2=}")
# set_1 > set_2=True
print(f"# {set_4 == set_2=}, {set_2 >= set_4=}, {set_2 <= set_4=}")
# set_4 == set_2=True, set_2 >= set_4=True, set_2 <= set_4=True
print(f"# {set_1 == set_3=}")
# set_1 == set_3=False
print(f"# {set_1 < set_3=}")
# set_1 < set_3=False
print(f"# {set_1 > set_3=}")
# set_1 > set_3=False
print(f"# {(set_1 != set_3)=}")
# (set_1 != set_3)=True
