list_s = [1,2,"3"]
list_s *= 3
print(f"# list_s *= 3\t: {list_s}")
# list_s *= 3	: [1, 2, '3', 1, 2, '3', 1, 2, '3']

del list_s[3:]
list_s+=["four"]
list_s.extend([5.0])
print(f"# list_s += b'de'\t: {list_s}")
# list_s += b'de'	: [1, 2, '3', 'four', 5.0]

list_s[3:]=[]
x = ["another item"]
list_s.append(x)
print(f"# list_s.append(x): {list_s}")
# list_s.append(x): [1, 2, '3', ['another item']]

print(f"# list_s.pop()\t: {list_s.pop()}, {list_s=}")
# list_s.pop()	: ['another item'], list_s=[1, 2, '3']

list_s.insert(2,x)
print(f"# list_s.insert(2,x): {list_s}")
# list_s.insert(2,x): [1, 2, ['another item'], '3']

list_s.remove(x)
print(f"# list_s.remove(x): {list_s}")
# list_s.remove(x): [1, 2, '3']

list_s.reverse()
print(f"# list_s.reverse(): {list_s}")
# list_s.reverse(): ['3', 2, 1]

list_s_copy = list_s.copy()
list_s.clear()
print(f"# list_s.clear\t: {list_s=}, {list_s_copy=}")
# list_s.clear	: list_s=[], list_s_copy=['3', 2, 1]
