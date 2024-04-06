"""Main script demonstrating importing into current namespace.

No functions, just demo from module import obj will bring obj into 
current namespace.
"""
"""save this as m6_2_4.py"""
from m6_1_circle import area as circle_area, circumference

print(f"# {'PI' in dir()=}, {'radius' in dir()=}")
# 'PI' in dir()=False, 'radius' in dir()=False

radius = 3
print(f"# {'radius' in dir()=}, {radius=}")
# 'radius' in dir()=True, radius=3

print(f"# {'circumference' in dir()=}, {circumference(radius)=}")
# 'circumference' in dir()=True, circumference(radius)=18.849555900000002

print(f"# {'area' in dir()=}, {'circle_area' in dir()=},"
      f" {circle_area(radius)=}")
# 'area' in dir()=False,'circle_area' in dir()=True, circle_area(radius)=28.27433385

def import_in_func() -> None:
      """Demo import can be done inside a function"""
      from m6_1_circle import PI
      print(f"# {'PI' in locals()=},{'PI' in globals()=}, {PI=}")

import_in_func()
# 'PI' in locals()=True,'PI' in globals()=False, PI=3.14159265
