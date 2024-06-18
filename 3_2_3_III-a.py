str_1 = "1 2"
match str_1.split():
    case first, '2' as second:
        print(f"# {first=}, {second=}")
    case _ as nomatch:
        print(f"# no pattern matched {nomatch}")
# first='1', second='2'

str_2 = "a,b,c,d,e,f,g"
match str_2.split(','):
    case 'a', 'b' as second, *middle, "g":
        print(f"# {second=}, {middle=}")
    case _ as nomatch:
        print(f"# no pattern matched {nomatch}")
# second='b', middle=['c', 'd', 'e', 'f']
