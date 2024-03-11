str_1 = "Hello World!"
str_1_as_dict = dict(enumerate(str_1))
print(f"# {str_1_as_dict=}")
# str_1_as_dict={0: 'H', 1: 'e', 2: 'l', 3: 'l', 4: 'o', 5: ' ', 6: 'W', 7: 'o', 8: 'r', 9: 'l', 10: 'd', 11: '!'}

match str_1_as_dict:
    case {0:"H" as val_1, 6:"W" as val_6, 11:"!" as val_11, **rest}:
        print(f"# {val_1=}, {val_6=}, {val_11=}, {rest=}")
    case _:
        print(f"# nope")

# val_1='H', val_6='W', val_11='!', rest={1: 'e', 2: 'l', 3: 'l', 4: 'o', 5: ' ', 7: 'o', 8: 'r', 9: 'l', 10: 'd'}
