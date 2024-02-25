str_2 = "a,b,c,d,e,f,g"
match str_2.split(','):
    case 'a', 'b' as second, *middle, "g" if 'x' in middle:
        print(f"# {second=}, {middle=}")
    case _ as nomatch:
        print(f"# no pattern matched {nomatch}")
        # no pattern matched ['a', 'b', 'c', 'd', 'e', 'f', 'g']

        
complex_1 = 3 + 5j
match complex_1:
    case complex(real = x, imag = 5) as complex_ if x == 4:
        print(f"# matched complex real portion is 4: {complex_}")
    case complex(real = x, imag = 4|5|6) as complex_ if x == 3:
        print(f"# matched complex real portion is 3: {complex_}")
        # matched complex real portion is 3: (3+5j)
    case _:
        print(f"# Error.")
