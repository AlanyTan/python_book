str_1="ABCDEF"
a,b,*rest,e,f=str_1
print(f"# {a=}, {b=}, {rest=}, {e=}, {f=}")
# a='A', b='B', rest=['C', 'D'], e='E', f='F'

list_1 = [1, 2, 3, 4, 5, 6]
*l_drop_last, _ = list_1
print(f"# {l_drop_last=}")
# l_drop_last=[1, 2, 3, 4, 5]

tuple_1 = ('a', 'b', 'c')
ti_1, ti_2, *t_rest = tuple_1
print(f"# {ti_1=}, {ti_2}, {t_rest=}")
# ti_1='a', b, t_rest=['c']

set_1 = {'one', 'two', 'three'}
si_1, *s_rest = set_1
print(f"# {si_1=}, {s_rest=}")
# si_1='two', s_rest=['one', 'three']

dict_1=dict(zip(tuple_1, set_1))
dk_1, dk_2, dk_3, *dk_rest = dict_1
print(f"# {dk_1=}, {dk_2=}, {dk_3=}, {dk_rest=}")
# dk_1='a', dk_2='b', dk_3='c', dk_rest=[]
