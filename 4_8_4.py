odd_sq_not_3 = ( x**2 for x in range(10) if x % 3)

for number in odd_sq_not_3:
    print(f"# next square not divisible by 3 is: {number}")
    
# next square not divisible by 3 is: 1
# next square not divisible by 3 is: 4
# next square not divisible by 3 is: 16
# next square not divisible by 3 is: 25
# next square not divisible by 3 is: 49
# next square not divisible by 3 is: 64
