print ("# not True is:", not True, ", not False is:", not False)
# not True is: False , not False is: True

print ("# not None is:", not None, ", not 'anything' is:", not "anything")
# not None is: True , not 'anything' is: False

numerator = 10
denominator = 2

divisible = denominator and not numerator % denominator and "Divisible"
divisible = divisible or "Not Divisible"
print("#", numerator, "/", denominator, "is", divisible)
# 10 / 2 is Divisible

denominator = 0

divisible = denominator and not numerator % denominator and "Divisible"
divisible = divisible or "Not Divisible"
print("#", numerator, "/", denominator, "is", divisible)
# 10 / 0 is Not Divisible
