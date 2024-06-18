complex_1 = 3 + 5j
match complex_1:
    case complex(real = x, imag = 5 as y) \
            as complex_alias if x**2 + y**2 >= 5**2:
        print(f"# {complex_alias=} is far from (0,0).")
    case complex(real = x, imag = 4|5|6 as y) as complex_alias if x == 3:
        print(f"# {complex_alias=} has real==3 and imag==4|5|6")
    case _:
        print(f"# Error.")
# complex_alias=(3+5j) is far from (0,0).

str_2 = "a,b,c,d,e,f,g"
match str_2:
    case _ as str_1 if str_1.startswith("a,c"):
        print(f"# {str_1=}")
    case _ as nomatch:
        print(f"# no pattern matched {nomatch}")
# no pattern matched a,b,c,d,e,f,g        
