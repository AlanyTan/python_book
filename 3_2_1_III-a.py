x = -1
if not x:
    print(f"# {x} is Falsy.")
    print(f"# cannot calculate {x}**(-1).")
elif x < 0:
    print(f"# {x} is negative.")
    print(f"# cannot calculate {x}**(1/2).")
elif x <= -1:
    print(f"#{x} is even smaller than -1")
    print(f"#But this block won't be executed")
else:
    print(f"# {x} is positive.")
    print(f"# {x} can be used as denominator or square of a root")
# -1 is negative.
# cannot calculate -1**(1/2).
