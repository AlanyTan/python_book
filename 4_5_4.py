def func_shadow_name() -> None:
    def len(v) -> str:
        return "len() has been shadowed."

    def abs(v) -> None:
        print(f"# printed from func_shadow_name's\n#   shadowed abs({v=})")

    abs(len('abc'))

func_shadow_name()
# printed from func_shadow_name's
#   shadowed abs(v='len() hse been shadowed.')

print(f"# calling abs() outside of func_shadow_name(): {abs(-10)=}")
# calling abs() outside of func_shadow_name(): abs(-10)=10

print(f"# calling len() outside of func_shadow_name(): {len('abc')=}")
# calling len() outside of func_shadow_name(): len('abc')=3
