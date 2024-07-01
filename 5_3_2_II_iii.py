str_1 = "ABCD"
byte_arr_1 = bytearray(b'EFGH')
list_1 = [1, '2.0', (3.0+4j)]

*list_begin, char_second_last, char_last = str_1
print(f"# {list_begin=}, {char_second_last=}, {char_last=}")
# list_begin=['A', 'B'], char_second_last='C', char_last='D'

int_first, *list_middle, int_last = byte_arr_1
print(f"# {int_first=}, {list_middle=}, {int_last=}")
# int_first=69, list_middle=[70, 71], int_last=72

int_first, str_second, *_ = list_1
print(f"# {int_first=}, {str_second=}, {_=}")
# int_first=1, str_second='2.0', _=[(3+4j)]

*list_no_tail, _ = byte_arr_1
print(f"# {list_no_tail=}")
# list_no_tail=[69, 70, 71]

list_2 = [[*str_1], *byte_arr_1]
print(f"# {list_2=}")
# list_2=[['A', 'B', 'C', 'D'], 69, 70, 71, 72]
[_, *list_sub_no_head], *rest, int_last = list_2
print(f"# {list_sub_no_head=}, {rest=}, {int_last=}")
# list_sub_no_head=['B', 'C', 'D'], rest=[69, 70, 71], int_last=72
