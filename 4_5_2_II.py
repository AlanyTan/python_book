def func_parent_scope(arg_p: str) -> str:
    """Demonstrate enclosing scope assigning

    Args:
        arg_p: argument to parent function

    Returns:
        the string returned by func_child which should be the 
            value of local_var
    """
    shadow_var = 'shdv'
    shd_var_alias = shadow_var
    enclosing_var = 'encv'
    enc_var_alias = enclosing_var
    def func_child_scope(arg_c: int) -> int:
        nonlocal enclosing_var
        print(f"#  -=func_child, {enclosing_var is enc_var_alias=}"
              f", {enclosing_var=}")
        enclosing_var = "enclosing_var from child"
        print(f"#  -=func_child, {enclosing_var is enc_var_alias=}"
              f", {enclosing_var=}")
        shadow_var = 'shadow_var from child'
        print(f"#  -=func_child, {shadow_var is shd_var_alias=}")
        return arg_c

    print(f"# -func_parent, {enclosing_var is enc_var_alias=}, {enclosing_var=}")
    print(f"# -func_parent, {shadow_var is shd_var_alias=}, {shadow_var=}")
    func_child_scope(0)
    print(f"# -func_parent, {enclosing_var is enc_var_alias=}, {enclosing_var=}")
    print(f"# -func_parent, {shadow_var is shd_var_alias=}, {shadow_var=}")
    return arg_p

print(f"# func returned:", func_parent_scope("from main"))
# -func_parent, enclosing_var is enc_var_alias=True, enclosing_var='encv'
# -func_parent, shadow_var is shd_var_alias=True, shadow_var='shdv'
#  -=func_child, enclosing_var is enc_var_alias=True, enclosing_var='encv'
#  -=func_child, enclosing_var is enc_var_alias=False, enclosing_var='enclosing_var from child'
#  -=func_child, shadow_var is shd_var_alias=False
# -func_parent, enclosing_var is enc_var_alias=False, enclosing_var='enclosing_var from child'
# -func_parent, shadow_var is shd_var_alias=True, shadow_var='shdv'
# func returned: from main
