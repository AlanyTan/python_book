"""Main script to demo from package import module"""
"""save this as m6_3_3_II.py"""
from m6_3_package.m6_3_2_geometry import circle
#DEBUG - m6_3_package(__init__.py:26) - m6_3_package/__init__.py Initializing package
#DEBUG - m6_3_2_geometry(__init__.py:29) -     in m6_3_2_package/m6_3_2_geometry/__init__.py, ['CONST_1', 'circle', 'logger', 'logging', 'perimeter', 'rectangle']

print("#=1.root level dir()", [d for d in dir() if not d.startswith('__')])
#=1.root level dir() ['circle']

from m6_3_package import m6_3_2_geometry

print("#=2.root level dir()", [d for d in dir() if not d.startswith('__')])
#=2.root level dir() ['circle', 'm6_3_2_geometry']
print(f"#=2.root level {circle is m6_3_2_geometry.circle=}")
#=2.root level circle is m6_3_2_geometry.circle=True

print(f"#=2.root level use obj from package: {m6_3_2_geometry.CONST_1=}")
#=2.root level use obj from package: m6_3_2_geometry.CONST_1='defined in sub package __init__.py'

from m6_3_package import module_1
#DEBUG - m6_3_package(module_1.py:9) -    m6_3_package/module_1.py root level, ['logger', 'logging', 'var_mod_1']

print("#=3.root level dir()", [d for d in dir() if not d.startswith('__')])
#=3.root level dir() ['circle', 'm6_3_2_geometry', 'module_1']
print("# ", module_1.func_in_mod_1())
#  func defined in module_1 under m6_3_package

radius = 3
print(f"# area of {radius=} is {circle.area(radius)}")
# area of radius=3 is 28.27433385

from m6_3_package.m6_3_2_geometry.circle import circumference

print(f"# circumference of {radius=} is {circumference(radius)}")
# circumference of radius=3 is 18.849555900000002

print("#=4.root_level_local_namespace globals:", *
      [(k, v) for k, v in globals().items() if not k.startswith('__')], sep='\n# ')
#=4.root_level_local_namespace globals:
# ('circle', <module 'm6_3_package.m6_3_2_geometry.circle' from 'C:\\Users\\user\\Documents\\python_book\\m6_3_package\\m6_3_2_geometry\\circle.py'>)
# ('m6_3_2_geometry', <module 'm6_3_package.m6_3_2_geometry' from 'C:\\Users\\user\\Documents\\python_book\\m6_3_package\\m6_3_2_geometry\\__init__.py'>)
# ('module_1', <module 'm6_3_package.module_1' from 'C:\\Users\\user\\Documents\\python_book\\m6_3_package\\module_1.py'>)
# ('radius', 3)
# ('circumference', <function circumference at 0x000001FE920823E0>)
