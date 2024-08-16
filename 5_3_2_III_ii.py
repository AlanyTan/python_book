list_s = [1, 2.0, ["3"]]
list_s *= 3
print(f"# list_s *= 3\t\t: {list_s}")
# list_s *= 3		: [1, 2.0, ['3'], 1, 2.0, ['3'], 1, 2.0, ['3']]

list_s[-1][0] = 4
print(f"# list_s[-1][0] = 4\t: {list_s}")
# list_s[-1][0] = 4	: [1, 2.0, [4], 1, 2.0, [4], 1, 2.0, [4]]

string_1 = "abc"
list_1 = ["xyz"]

list_s[3:] = []
list_s.append(string_1)
print(f"# list_s.append(s)\t: {list_s}")
# list_s.append(s)	: [1, 2.0, [4], 'abc']
list_s.append(list_1)
print(f"# list_s.append(l)\t: {list_s}")
# list_s.append(l)	: [1, 2.0, [4], 'abc', ['xyz']]


del list_s[2:]
list_s += string_1
print(f"# list_s += s\t\t: {list_s}")
# list_s += s		: [1, 2.0, 'a', 'b', 'c']
list_s[len(list_s):] = string_1
print(f"# list_s[len(list_s):]=s: {list_s}")
# cs: [1, 2.0, 'a', 'b', 'c', 'a', 'b', 'c']
list_s.extend(string_1)
print(f"# list_s.extend(s)\t: {list_s}")
# list_s.extend(s)	: [1, 2.0, 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']
list_s.extend([string_1])
print(f"# list_s.extend(s)\t: {list_s}")
# list_s.extend([s])	: [1, 2.0, 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'abc']

list_s = list_s[:2]
list_s += list_1
print(f"# list_s += l\t\t: {list_s}")
# list_s += l		: [1, 2.0, 'xyz']
list_s[len(list_s):] = list_1
print(f"# list_s[len(list_s):]=l: {list_s}")
# list_s[len(list_s):]=l: [1, 2.0, 'xyz', 'xyz']
list_s.extend(list_1)
print(f"# list_s.extend(l)\t: {list_s}")
# list_s.extend(l)	: [1, 2.0, 'xyz', 'xyz', 'xyz']
list_s.extend([list_1])
print(f"# list_s.extend([l])\t: {list_s}")
# list_s.extend([l])	: [1, 2.0, 'xyz', 'xyz', 'xyz', ['xyz']]

print(f"# list_s.pop()\t\t: {list_s.pop()}, {list_s=}")
# list_s.pop()		: ['xyz'], list_s=[1, 2.0, 'xyz', 'xyz', 'xyz']

print(f"# list_s.pop(1)\t\t: {list_s.pop(1)}, {list_s=}")
# list_s.pop(1)		: 2.0, list_s=[1, 'xyz', 'xyz', 'xyz']

list_s.insert(2, string_1)
print(f"# list_s.insert(2.0,s)\t: {list_s}")
# list_s.insert(2.0,s)	: [1, 'xyz', 'abc', 'xyz', 'xyz']

list_s.remove(list_s[-1])
print(f"# list_s.remove(list_s[-1])\t: {list_s}")
# list_s.remove(list_s[-1])	: [1, 'abc', 'xyz', 'xyz']
list_s.remove(string_1)
print(f"# list_s.remove(s)\t: {list_s}")
# list_s.remove(s)	: [1, 'xyz', 'xyz']

list_s.reverse()
print(f"# list_s.reverse()\t: {list_s}")
# list_s.reverse()	: ['xyz', 2.0, 1]

list_s_copy = list_s.copy()
list_s.clear()
print(f"# list_s.clear\t\t: {list_s=}, {list_s_copy=}")
# list_s.clear		: list_s=[], list_s_copy=['xyz', 2.0, 1]
