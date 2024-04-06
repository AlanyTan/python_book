"""Demonstrate definition and import of modules.

Includes functions to calculate the circumference and area of 
a circle. PI is defined internally as a constant.
"""
"""save this as m6_1_2_II_circle.py"""
PI = 3.14159265

def circumference (r: int|float) -> float:
    """Calculate circumference of a circle with radius=r.
    
    Args:
        r: radius of the circle.
    
    Returns:
        the circumference of the circle.
    """
    return r * 2 * PI

def area (r: int|float) -> float:
    """Calcuate area of a circle with radius=r

    Args:
        r: radius of the circle.
    
    Returns:
        the area of the circle.
    
    """
    return r**2 * PI
