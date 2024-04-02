def f(x) -> float:
    """Calculates the circumference of a circle given its radius.

    Args:
        x (float): The radius of the circle.

    Returns:
        float: The circumference of the circle.
    """
    PI = 3.14159
    circumference = 2*PI*x
    return circumference

radius = 2
print(f"# {f(radius)=}")
# f(radius)=12.56636
