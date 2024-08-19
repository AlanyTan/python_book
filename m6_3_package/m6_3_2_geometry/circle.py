"""Part of demo of package structure, calculate circle area and circumference.

Functions:
    circumference(r): calculate the circumference of a circle with radius r
    area(r): calculate the area for a circle with radius r
"""
"""save this as m6_3_package/m6_3_2_geometry/circle.py"""

PI = 3.14159265


def circumference(r: float | int) -> float:
    """calculate circle circumference

    Args:
        r: the radius of the circle

    Returns:
        a number representing the circle's circumference.
    """
    return r * 2 * PI


def area(r: float | int) -> float:
    """calculate circle area

    Args:
        r: the radius of the circle

    Returns:
        a number representing the circle's area.
    """
    return r**2 * PI


def main():
    """if this file is called directly run some tests"""
    r = 2
    print(f"testing r={r} circumference is {circumference(r)}")
    print(f"testing r={r} area is {area(r)}")


if __name__ == "__main__":
    main()
