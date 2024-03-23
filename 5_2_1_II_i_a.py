str_1="ABCDEF"

a,b,c,d,e,f=str_1
print(f"# {a=}, {b=}, {c=}, {d=}, {e=}, {f=}")
# a='A', b='B', c='C', d='D', e='E', f='F'

a,b,*rest,e,f=str_1
print(f"# {a=}, {b=}, {rest=}, {e=}, {f=}")
# a='A', b='B', rest=['C', 'D'], e='E', f='F'
