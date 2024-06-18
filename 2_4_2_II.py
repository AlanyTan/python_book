print("#", True and True, True and False, False and True, False and False)
# True False False False

print("#", 2 and True and "3" and 5.0 and 0 and False and 0.0)
# 0

print("#", 2 and True and "3" and 5.0)
# 5.0

dividend = 5
divisor = 0
print("# divided:", divisor != 0 and dividend / divisor)
# divided: False
