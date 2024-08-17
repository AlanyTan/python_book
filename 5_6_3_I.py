list_1 = ['one', 'two', 'three']
range_1 = range(3)
dict_1 = dict(zip(list_1, range_1))
print("#", *dict_1)
# one two three

key_1, key_2, key_3 = dict_1
print(f"# {key_1=},{key_2=},{key_3=}. "
      f"{dict_1[key_1]=}. {dict_1[key_2]=}. {dict_1[key_3]=}")
# key_1='one',key_2='two',key_3='three'. dict_1[key_1]=0. dict_1[key_2]=1. dict_1[key_3]=2

key_1, *rest = dict_1
print(f"# {key_1=}, {rest=}. "
      f"{dict_1[key_1]=}, {dict_1[rest[0]]=}, {dict_1[rest[1]]=}")
# key_1='one', rest=['two', 'three']. dict_1[key_1]=0, dict_1[rest[0]]=1, dict_1[rest[1]]=2
