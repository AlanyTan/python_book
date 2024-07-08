def func_shadow_buildins() -> None:
    """Demonstrate what should be avoided:
    shadowing of buildin function and variable.

    Args:
        None.

    Returns:
        None
    """
    def len(v) -> str:
        return f"len({v}) has been shadowed."

    print(f"# -=in func_shadow_buildins: {len('abc')=}")


print(f"# in main before, {len('abc')=}")
# in main before, len('abc')=3

func_shadow_buildins()
# -=in func_shadow_buildins: len('abc')='len(abc) has been shadowed.'

print(f"# in main after, {len('abc')=}")
# in main after, len('abc')=3
