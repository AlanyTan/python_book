var_a, var_b, var_c = "ABC"
print(f"# {var_a=}, {var_b=}, {var_c=}")
# var_a='A', var_b='B', var_c='C'

list_1 = [1, 2, 3, 4, 5, 6]
li_1, li_2, li_3 = list_1[:3]
print(f"# {li_1=}, {li_2=}, {li_3=}")
# li_1=1, li_2=2, li_3=3

tuple_1 = ('a', 'b', 'c')
ti_1, ti_2, ti_3 = tuple_1
print(f"# {ti_1=}, {ti_2}, {ti_3=}")
# ti_1='a', b, ti_3='c'

set_1 = {'one', 'two', 'three'}
si_1, si_2, si_3 = set_1
print(f"# {si_1=}, {si_2=}, {si_3=}")
# si_1='two', si_2='one', si_3='three'

dict_1 = dict(zip(tuple_1, set_1))
dk_1, dk_2, dk_3 = dict_1
print(f"# {dk_1=}, {dk_2=}, {dk_3=}")
# dk_1='a', dk_2='b', dk_3='c'
