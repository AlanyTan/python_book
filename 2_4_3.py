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
print("# b == a:", b == a, ", b is a:", b is a, ", b is True: ", b is True)
# b == a: True , b is a: False , b is True:  True

print("# b * 2 == a * 2:", b * 2 is a * 2)
# b * 2 == a * 2: True

d = c = False
print("# b + c > c + d:", b + c > d)
# b + c > d: True
