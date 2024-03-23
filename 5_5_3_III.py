tuple_1 = (1,"2",3.0)
tuple_1_alias = tuple_1[:]
tuple_1_again = 1,"2",3.0
print(f"# {tuple_1 == tuple_1_alias=}, {tuple_1 is tuple_1_alias=}")
# tuple_1 == tuple_1_alias=True, tuple_1 is tuple_1_alias=True

print(f"# {tuple_1 == tuple_1_again=}, {tuple_1 is tuple_1_again=}")
# tuple_1 == tuple_1_again=True, tuple_1 is tuple_1_again=True

print(f"# {tuple_1 in tuple_1_again=}, {tuple_1[0] in tuple_1_again=}")
# tuple_1 in tuple_1_again=False, tuple_1[0] in tuple_1_again=True

tuple_2 = ([1],"3",4.0)
tuple_2_alias = tuple_2[:]
tuple_2_copy = (*tuple_2,)
tuple_2_again =  ([1],"3",4.0)
print(f"# {tuple_2 == tuple_2_alias=}, {tuple_2 is tuple_2_alias=}")
# tuple_2 == tuple_2_alias=True, tuple_2 is tuple_2_alias=True

print(f"# {tuple_2 == tuple_2_copy=}, {tuple_2 is tuple_2_copy=}")
# tuple_2 == tuple_2_copy=True, tuple_2 is tuple_2_copy=False

print(f"# {tuple_2[0] == tuple_2_copy[0]=}, {tuple_2[0] is tuple_2_copy[0]=}")
# tuple_2[0] == tuple_2_copy[0]=True, tuple_2[0] is tuple_2_copy[0]=True

print(f"# {tuple_2 == tuple_2_again=}, {tuple_2 is tuple_2_again=}")
# tuple_2 == tuple_2_again=True, tuple_2 is tuple_2_again=False

print(f"# {tuple_2[0] == tuple_2_again[0]=}, {tuple_2[0] is tuple_2_again[0]=}")
# tuple_2[0] == tuple_2_again[0]=True, tuple_2[0] is tuple_2_again[0]=False

tuple_2[0].append("2")
print(f"# {tuple_2_alias}, {tuple_2_copy=}, {tuple_2_again=}")
# ([1, '2'], '3', 4.0), tuple_2_copy=([1, '2'], '3', 4.0), tuple_2_again=([1], '3', 4.0)

print(f"# {tuple_2 > tuple_2_again=}")
# tuple_2 > tuple_2_again=True

print(f"# {(1,2,5) > (1,2,3,4,5,6)=}")
# (1,2,5) > (1,2,3,4,5,6)=True

print(f"# {(1,) < (1,'2')=}")
# (1,) < (1,'2')=True
