rectangle_tuple_1 = (3, 4, 5)
length, width, height = rectangle_tuple_1
print(f"# {length=}, {width=}, {height=}")
# length=3, width=4, height=5

employee_tuple_1 = 1, "John Sam", "Male", "1990/09/09", "11010920000101111", \
    "2020/01"
emp_id, name, sex, dob, *rest = employee_tuple_1

print(f"# {emp_id=}, {name=}, {sex=}, {dob=}")
# emp_id=1, name='John Sam', sex='Male', dob='1990/09/09', hire_year='11010920000101111'

print(f"# {rest=}")
# rest=['11010920000101111', '2020/01']
