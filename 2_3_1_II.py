x = 10
y = 3.0
z = (2 + 1j)

sum_ = x + x
print("#", sum_, type(sum_))
# 20 <class 'int'>

difference = x - y
print("#", difference, type(difference))
# 7.0 <class 'float'>

product = x * z
print("#", product, type(product))
# (20+10j) <class 'complex'>

quotient = x / 2
print("#", quotient, type(quotient))
# 5.0 <class 'float'>

exponential = z ** 2
print("#", exponential, type(exponential))
# (3+4j) <class 'complex'>

euclidean_quotient = x // y
print("#", euclidean_quotient, type(euclidean_quotient))
# 3.0 <class 'float'>

remainder = x % 4
print("#", remainder, type(remainder))
# 2 <class 'int'>

complex_parts = z * 0
print("#", complex_parts, type(complex_parts))
print("#", complex_parts.real, type(complex_parts.real))
print("#", complex_parts.imag, type(complex_parts.imag))
# 0j <class 'complex'>
# 0.0 <class 'float'>
# 0.0 <class 'float'>
