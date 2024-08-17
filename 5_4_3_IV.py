tuple_example = (1, 2, "3", "four", 5.0, 1)

print(f"# count of 1: {tuple_example.count(1)}")
# count of 1: 2

print(f"# count of \"3\": {tuple_example.count('3')}")
# count of "3": 1

print(f"# which item matches \"3\": {tuple_example.index('3')}")
# which item matches "3": 2

print(f"# start from 2nd, which item matches 1: {tuple_example.index(1, 1)}")
# after 2nd position, which item matches 1: 5
