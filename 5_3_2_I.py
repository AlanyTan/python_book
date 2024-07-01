print(f"# {[1,2,[3,4]][1]=}")
# [1,2,[3,4]][1]=2

print(f"# {[1,2,[3,4]][2][1]=}")
# [1,2,[3,4]][2][1]=4

list_example=[1,2.0,"3","four", ['a', 'b', 'c']]
print(f"# {list_example[-1][0]=}")
# list_example[-1][0]='a'

print(f"# {list_example[-1][::-1]=}")
# list_example[-1][::-1]=['c', 'b', 'a']

print(f"# {list_example[::2][::-1]=}")
# list_example[::2][::-1]=[['a', 'b', 'c'], '3', 1]
