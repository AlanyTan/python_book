def func_shadow_buildins() -> None:
    """Demonstrate what should be avoided:
    shadowing of buildin function and variable.

    Args:
        None.

    Returns:
        None
    """
    def len(v) -> str:
        return "len() has been shadowed."

    __file__ = 'shadowed filename.'
    print(f"# -=in func_shadow_buildins: {len('abc')=}, {__file__=}")


print(f"# in main before, {len('abc')=}, {__file__=}")
# in main before, len('abc')=3, __file__='/home/alan/Documents/Python.book/4_5_4.py'

func_shadow_buildins()
# -=in func_shadow_buildins: len('abc')='len() has been shadowed.', __file__='shadowed filename.'

print(f"# in main after, {len('abc')=}, {__file__=}")
# in main after, len('abc')=3, __file__='/home/alan/Documents/Python.book/4_5_4.py'
