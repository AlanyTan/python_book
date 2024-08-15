"""Main script to demo import package"""
"""save this as m6_3_3_I.py"""

import m6_3_package
#DEBUG - m6_3_package(__init__.py:26) - m6_3_package/__init__.py Initializing package

print("#=1.root level globals:"
        , *[(k, v) for k, v in globals().items() if not k.startswith('__')]
        , sep='\n# ')
#=1.root level globals:
# ('m6_3_package', <module 'm6_3_package' from 'C:\\Users\\user\\Documents\\python_book\\m6_3_package\\__init__.py'>)
print("#=1.root level dir(m6_3_package)"
      , [d for d in dir(m6_3_package) if not d.startswith('__')])
#=1.root level dir(m6_3_package) ['func_in_init', 'logger', 'logging']
print("#=1.root level call func_in_init:", m6_3_package.func_in_init())
#=1.root level call func_in_init: in func_in_init of m6_3_package

import m6_3_package.module_1 as mod_1
#DEBUG - m6_3_package(module_1.py:9) -    m6_3_package/module_1.py root level, ['logger', 'logging', 'var_mod_1']

print("#=2.root level globals:"
        , *[(k, v) for k, v in globals().items() if not k.startswith('__')]
        , sep='\n# ')
#=2.root level globals:
# ('m6_3_package', <module 'm6_3_package' from 'C:\\Users\\user\\Documents\\python_book\\m6_3_package\\__init__.py'>)
# ('mod_1', <module 'm6_3_package.module_1' from 'C:\\Users\\user\\Documents\\python_book\\m6_3_package\\module_1.py'>)
print("#=2.root level dir(m6_3_package)"
      , [d for d in dir(m6_3_package) if not d.startswith('__')])
#=2.root level dir(m6_3_package) ['func_in_init', 'logger', 'logging', 'module_1']
print("#=2.root level dir(mod_1)", [d for d in dir(mod_1) if not d.startswith('__')])
#=2.root level dir(mod_1) ['func_in_mod_1', 'logger', 'logging', 'var_mod_1']
print(f"#=2.root level "
      "{mod_1.func_in_mod_1 is m6_3_package.module_1.func_in_mod_1=}")
#=2.root level {mod_1.func_in_mod_1 is m6_3_package.module_1.func_in_mod_1=}

import m6_3_package.m6_3_2_geometry.circle
#DEBUG - m6_3_2_geometry(__init__.py:29) -     in m6_3_2_package/m6_3_2_geometry/__init__.py, ['CONST_1', 'circle', 'logger', 'logging', 'perimeter', 'rectangle']

import m6_3_package.m6_3_2_geometry.rectangle as rect

print("#=3.root level dir(m6_3_package)"
      , [d for d in dir(m6_3_package) if not d.startswith('__')])
#=3.root level dir(m6_3_package) ['func_in_init', 'logger', 'logging', 'm6_3_2_geometry', 'module_1']
print("#==3.package level dir(m6_3_package.m6_3_2_geometry)", 
      [d for d in dir(m6_3_package.m6_3_2_geometry) if not d.startswith('__')])
#==3.package level dir(m6_3_package.m6_3_2_geometry) ['CONST_1', 'circle', 'logger', 'logging', 'perimeter', 'rectangle']
print("#===3.subpackage level dir(..circle)", 
      [d for d in dir(m6_3_package.m6_3_2_geometry.circle) 
       if not d.startswith('__')])
#===3.subpackage level dir(..circle) ['PI', 'area', 'circumference', 'main']

radius = 3
print(f"# area of a circle with r={radius} is "
      f"{m6_3_package.m6_3_2_geometry.circle.area(radius)}")
# area of a circle with r=3 is 28.27433385

length=4
print(f"# perimeter of square {length=} is {rect.perimeter(length)}")
# perimeter of square length=4 is 16
