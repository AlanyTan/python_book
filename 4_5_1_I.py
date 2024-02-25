def func_local_scope(arg_l: str) -> str:
    local_var = 'locv'
    print(f"# - func_local, arg_l exist: {'arg_l' in dir()}, {arg_l=}")
    print(f"# - func_local, local_var exist: {'local_var' in dir()},\
        {local_var=}")
    return local_var

print(f"# func returned:", func_local_scope("anything"))
# - func_local, arg_l exist: True, arg_l='anything'
# - func_local, local_var exist: True,        local_var='locv'
# func returned: locv

print(f"# outside, arg_l exist: {'arg_l' in dir()}")
# outside, arg_l exist: False

print(f"# outside func, local_var exist: {'local_var' in dir()}")
# outside func, local_var exist: False    
