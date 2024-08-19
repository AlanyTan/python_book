set_1_alias = set_1 = {1, "2", 3.0}
set_2 = {3, "4", 1}
set_2_copy = {*set_2}
print(f"# {set_1 | set_2=}, {set_1 & set_2=}")
# set_1 | set_2={1, 3.0, '4', '2'}, set_1 & set_2={1, 3}

set_1 |= set_2
print(f"# {set_1=}, {set_1 is set_1_alias=}")
# set_1={1, 3.0, '4', '2'}, set_1 is set_1_alias=True
set_2 |= set_1
print(f"# {set_2=}, {set_2_copy=}")
# set_2={'4', 1, 3, '2'}, set_2_copy={'4', 3, 1}

set_1_alias = set_1 = {1, "2", 3.0}
set_2 = {3, "4", 1}
set_2_copy = {*set_2}
set_2 &= set_1
print(f"# {set_2=}, {set_2_copy=}")
# set_2={1, 3.0}, set_2_copy={'4', 3, 1}
set_1 &= set_2_copy
print(f"# {set_1=}, {set_1 is set_1_alias=}")
# set_1={1, 3}, set_1 is set_1_alias=True
