print("#", 2 + 3.0 or 10 - 4)
# 5.0
print("#",2 + (3.0 and 10) - 4)
# 8

print("#", 2 + 3.0 and 10 - 7 == 5)
# False
print("#",(2 + 3.0 or 10 - 7) == 5)
# True

print("#", 2 + 3.0 and 10 - (4 == 4))
# 9
print("#", 2 + (3.0 or 10) - (4 == 4))
#4.0

print("#", variable_1 := 2 + 3.0 and not 10 - 1 == 10, variable_1)
# True True
print("#", (variable_1 := 2 + 3.0) and not 10 - 1 == 10, variable_1)
# True 5.0
