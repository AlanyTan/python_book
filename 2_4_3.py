print("#", True == True, True is True)
# True True

print("#", False == True, False is False)
# False True

print("#", True == 1, True is 1)
# True False

print("#", False == 0, False is 0)
# True False

a = 1
b = True
print("#", b == a, b == a * 2, a*2 != 0)
# True False True

print("#", b * 2 is a * 2)
# True
