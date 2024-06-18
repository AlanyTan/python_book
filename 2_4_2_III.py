print ("# not True is:", not True, ", not False is:", not False)
# not True is: False , not False is: True

print ("# not None is:", not None, ", not 'anything' is:", not "anything")
# not None is: True , not 'anything' is: False

dividend = 10
divisor = 2
divisible = divisor and not dividend % divisor and "Divisible"
divisible = divisible or "Not Divisible"
print("#", dividend, "/", divisor, "is", divisible)
# 10 / 2 is Divisible

divisor = 0
divisible = divisor and not dividend % divisor and "Divisible"
divisible = divisible or "Not Divisible"
print("#", dividend, "/", divisor, "is", divisible)
# 10 / 0 is Not Divisible
