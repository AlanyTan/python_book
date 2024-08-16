buffer_list = []
while (new_string := input("#   ?:")) or buffer_list:
    buffer_list.extend(new_string)
    print(f"# Processing:{buffer_list.pop(0)}, still in queue:{buffer_list}")
#   ?:abc
# Processing:a, still in queue:['b', 'c']
#   ?:
# Processing:b, still in queue:['c']
#   ?:de
# Processing:c, still in queue:['d', 'e']
#   ?:
# Processing:d, still in queue:['e']
#   ?:
# Processing:e, still in queue:[]
#   ?:
