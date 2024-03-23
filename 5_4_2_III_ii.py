list_1 = [1,"2",3.0]
list_2 = ["Four", 5]
str_1 = "abc"

print(f"# {[*list_1, *list_2]=}")
# list_1 + list_2=[1, '2', 3.0, 'Four', 5]

print(f"# {[*list_1, *str_1, "y", "z"]=}")
# [*list_1, *str_1, "y", "z"]=[1, '2', 3.0, 'a', 'b', 'c', 'y', 'z']
