print ("#", not True, not False)
# False True

print ("#", not None, not "anything")
# True False

numerator = 10
denominator = 5

if denominator == 0 or numerator % denominator:
    print("# Not divisible")
else:
    print("# Divisible")
# Divisible

denominator = 0
if denominator and not numerator % denominator:
    print("# Divisible")
else:
    print("# Not divisible")
# Not divisible
