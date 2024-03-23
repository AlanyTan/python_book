ba_alias = ba_s = bytearray(b'abc')
ba_s *= 3
print(f"# ba_s *= 3\t: {ba_s}, still same: {ba_alias is ba_s}")
# ba_s *= 3	: bytearray(b'abcabcabc'), still same: True

del ba_s[3:]
ba_s+=b'de'
print(f"# ba_s += b'de'\t: {ba_s} still same: {ba_alias is ba_s}")
# ba_s *= 3	: bytearray(b'abcabcabc'), still same: True

ba_s[3:]=[]
x = 0X44
ba_s.append(x)
print(f"# ba_s.append(x): {ba_s}")
# ba_s.append(x): bytearray(b'abcD')

print(f"# ba_s.pop()\t: {ba_s.pop()}, {ba_s=}")
# ba_s.pop()	: 68, ba_s=bytearray(b'abc')

ba_s.insert(2,x)
print(f"# ba_s.insert(2,x): {ba_s}")
# ba_s.insert(2,x): bytearray(b'abDc')

ba_s.remove(x)
print(f"# ba_s.remove(x): {ba_s}")
# ba_s.remove(x): bytearray(b'abc')

ba_s.reverse()
print(f"# ba_s.reverse(): {ba_s}")
# ba_s.reverse(): bytearray(b'cba')

ba_s_copy = ba_s.copy()
ba_s.clear()
print(f"# ba_s.clear\t: {ba_alias=}, {ba_s_copy=}")
# ba_s.clear	: ba_alias=bytearray(b''), ba_s_copy=bytearray(b'cba')
