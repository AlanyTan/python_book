def func_local_scope(arg_l: str) -> str:
    var = 0
    print(f"# - func_local, var exist: {var is var_alias=}, {var=}")    
    return arg_l[:3]

var = "main scope"
var_alias = var

print(f"# func returned:", func_local_scope("anything"))
# - func_local, var exist: var is var_alias=False, var=0
# func returned: any

print(f"# outside, var exist: {'var' in dir()}, {var is var_alias=}, {var=}")
# outside, var exist: True, var is var_alias=True, var='main scope'
