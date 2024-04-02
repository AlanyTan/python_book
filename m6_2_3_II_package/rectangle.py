#save this as m6_2_3_II_package/rectangle.py
def perimeter (a,b=None):
    if b == None:
        b = a
    return 2*(a+b)

def area (a,b=None):
    if b == None:
        b = a
    return a*b
