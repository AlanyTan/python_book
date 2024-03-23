rectangle_tuple_1 = (3, 4, 5)
print(f"# {rectangle_tuple_1=}")
# rectangle_tuple_1=(3, 4, 5)

employee_tuple_1 = 1, "John Sam", "Male", "1990/09/09", "11010920000101111",\
                 "2020/01"
print(f"# {employee_tuple_1=}")
# employee_tuple_1=(1, 'John Sam', 'Male', '1990/09/09', '11010920000101111', '2020/01')

def func_return_packing(rec: tuple) -> tuple:
    return 2*(rec[0]*rec[1] + rec[1]*rec[2] + rec[0]*rec[2]), \
           rec[0]*rec[1]*rec[2]

return_tuple = func_return_packing((3,4,5))
print(f"# {return_tuple=}")
# return_tuple=(94, 60)
