str_1 = "Hello World!"
match dict(enumerate(str_1)):
    case {0:"H" as val_1, 6:"W" as val_6}:
        print(f"# {val_1=}, {val_6=}")
        # val_1='H', val_6='W'
    case _:
        print(f"# nope")

str_2 = "Hello Python!"
match dict(enumerate(str_2[:7])):
    case {0:"H" as val_1, 6:_ as val_6, **rest}:
        print(f"# {val_1=}, {val_6=}")
        # val_1='H', val_6='P'
        print(f"#  and {rest=}")
        #  and rest={1: 'e', 2: 'l', 3: 'l', 4: 'o', 5: ' '}
    case _:
        print(f"# nope")
