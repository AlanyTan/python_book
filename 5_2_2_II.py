def test_var_is(arg_1: int, arg_2: bytearray) -> bool:
    print(f"# - {arg_1 is int_1=}, {arg_2 is ba_1=}")
    arg_1 += 1
    arg_2 += b'array'
    print(f"# - {arg_1 is int_1=}, {arg_2 is ba_1=}")

int_1 = 1
int_2 = int_1

ba_1 = bytearray(b'byte')
ba_2 = ba_1

test_var_is(int_1, ba_1)
# - arg_1 is int_1=True, arg_2 is ba_1=True
# - arg_1 is int_1=False, arg_2 is ba_1=True

print(f"# {int_1 is int_2=}, {ba_1 is ba_2=}")
# int_1 is int_2=True, ba_1 is ba_2=True

int_1 *= 2
ba_1 *= 2
print(f"# {int_1 is int_2=}, {ba_1 is ba_2=}, {ba_2=}")
# int_1 is int_2=False, ba_1 is ba_2=True, ba_2=bytearray(b'bytearraybytearray')
