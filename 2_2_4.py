a = 3
b = a
print("#", a, b)
# 3 3
print("#", a is b)
# True

b = 7
print("#", a, b)
# 3 7
print("#", a is b)
# False

a = [3]
b = [3]
print("#", a, b)
# [3] [3]
print("#", a is b)
# False

a.append(7)
print("#", a, b)
# [3, 7] [3]
print("#", a is b)
# False

b = a = [3]
print("#", a, b)
# [3] [3]
print("#", a is b)
# True

a.append(7)
print("#", a, b)
# [3, 7] [3, 7]
print("#", a is b)
# True
