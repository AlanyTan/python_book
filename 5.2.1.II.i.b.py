str_1="ABCDEF"

a_1,b_1,c_1,d_1,e_1,f_1=str_1
print(f"# {a_1=}, {b_1=}, {c_1=}, {d_1=}, {e_1=}, {f_1=}")
# a_1='A', b_1='B', c_1='C', d_1='D', e_1='E', f_1='F'

a_2,b_2,*rest,e_2,f_2=str_1
print(f"# {a_2=}, {b_2=}, {rest=}, {e_2=}, {f_2}")

# a_2='A', b_2='B', rest=['C', 'D'], e_2='E', F