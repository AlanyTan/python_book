def func_parent_scope(arg_p: str) -> str:
    enclosing_var = 'encv'
    def func_child_scope(arg_c: int) -> str:
        local_var = 'locv'
        print(f"#   -= func_child, arg_c exist: {'arg_c' in dir()\
        }, \t{arg_c=}")
        print(f"#   -= func_child, arg_p exist: {'arg_p' in dir()\
        }, \t{arg_p=}")
        print(f"#   -= func_child, local_var exist: {'local_var' in dir()\
        }, \t{local_var=}")
        print(f"#   -= func_child, enclosing_var exist: {'enclosing_var' \
        in dir()}, \t{enclosing_var=}")
        return local_var
    
    print(f"# - func_parent, arg_p exist: {'arg_p' in dir()}, \t{arg_p=}")
    print(f"# - func_parent, enclosing_var exist: {'enclosing_var' in dir()\
        }, \t{enclosing_var=}")
    print(f"# - func_parent, arg_c exist: {'arg_c' in dir()}")
    print(f"# - func_parent, local_var exist: {'local_var' in dir()},")
    return func_child_scope(0)

print(f"# func returned:", func_parent_scope("anything"))
# - func_parent, arg_p exist: True, 	arg_p='anything'
# - func_parent, enclosing_var exist: True, 	enclosing_var='encv'
# - func_parent, arg_c exist: False
# - func_parent, local_var exist: False,
#   -= func_child, arg_c exist: True, 	arg_c=0
#   -= func_child, arg_p exist: True, 	arg_p='anything'
#   -= func_child, local_var exist: True, 	local_var='locv'
#   -= func_child, enclosing_var exist: True, 	enclosing_var='encv'
# func returned: locv

print(f"# outside, arg_p exist: {'arg_p' in dir()}")
# outside, arg_p exist: False

print(f"# outside, local_var exist: {'local_var' in dir()}")
# outside, local_var exist: False    

print(f"# outside, enclosing_var exist: {'enclosing_var' in dir()}")
# outside, enclosing_var exist: False
