def f(x)->float:
    """
    Calculate the circumference of a circle with a radius of x.

    Args:
        x:  int | float
          the radius of the circle.

    Returns:
        A float representing the circumference of the circle.
    """
    PI = 3.14159
    circumference = 2 * PI * x
    return circumference
