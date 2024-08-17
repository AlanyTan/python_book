rectangle_tuple_1 = (3, 4, 5)
print(f"# {rectangle_tuple_1=}")
# rectangle_tuple_1=(3, 4, 5)

employee_tuple_1 = 1, "John Sam", "Male", "1990/09/09", "11010920000101111", \
    "2020/01"
print(f"# {employee_tuple_1=}")
# employee_tuple_1=(1, 'John Sam', 'Male', '1990/09/09', '11010920000101111', '2020/01')

single_item_tuple = 'abc',
print(f"# {single_item_tuple=}")
# single_item_tuple=('abc',)


def func_return_packing(rect: tuple) -> tuple:
    """Calculate surface are and volume of a prism.
    Args:
        (length, width, depth): tuple of 3 numbers.

    Returns:
        a tuple (surface_area, volume)
    """
    return 2 * (rect[0] * rect[1] + rect[1] * rect[2] + rect[0] * rect[2]), \
        rect[0] * rect[1] * rect[2]


return_tuple = func_return_packing((3, 4, 5))
print(f"# {return_tuple=}")
# return_tuple=(94, 60)
