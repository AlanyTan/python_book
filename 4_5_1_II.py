def func_local_scope(arg_l: str) -> str:
    """Demonstrate variable shadowing

    Args:
        arg_l: an argument used to demonstrate arguments are local scoped

    Returns:
        A string that was the value of the arg_l 
    """

    var = "local scope"
    print(f"# -in func_local_scope, {var is var_alias=}, {var=}, {var_alias=}")
    return arg_l


var = "main scope"
var_alias = var
print(f"# in main, var exist: {'var' in dir()}, {var is var_alias=}, {var=}")
# in main, var exist: True, var is var_alias=True, var='main scope'

print(f"# in main, {func_local_scope(var)=}")
# -in func_local, var is var_alias=False, var='local scope', var_alias='main scope'
# in main, func_local_scope(var)='main scope'

print(f"# in main, var exist: {'var' in dir()}, {var is var_alias=}, {var=}")
# in main, var exist: True, var is var_alias=True, var='main scope'
