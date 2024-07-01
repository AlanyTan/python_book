def func_return_packing(*rect: tuple) -> tuple:
    """Take 3 args as length, width, depth and calculate surface are and volume
    Args:
        length:
        width:
        depth:

    Returns:
        a tuple (surface_area, volume)
    """
    return 2*(rect[0]*rect[1] + rect[1]*rect[2] + rect[0]*rect[2]), \
           rect[0]*rect[1]*rect[2]

return_tuple = func_return_packing(3,4,5)
print(f"# {return_tuple=}")
# return_tuple=(94, 60)
