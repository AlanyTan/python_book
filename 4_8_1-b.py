from collections.abc import Generator


def counter(arg_1: int, arg_2: int | None = None,
            step: int = 1) -> Generator[int]:
    """A counter generator with start, stop, step parameters.

    Args:
        arg_1: required, if used by itself, counter starts from 0 and stops 
            before this number; if arg_2 is provided, starts from this number
        arg_2: optional, if provided, counter starts from arg_1 and stops
            before this number.
        step: optional, the step size between each yield.

    Yields:
        a the current counter number
    """
    if arg_2 is None:
        start = 0
        stop = arg_1
    else:
        start = arg_1
        stop = arg_2

    sign = 1 if start < stop else -1
    if step * sign < 0:
        current = stop
    else:
        current = start

    while current * sign < stop * sign:
        print(f"# -in generator {current=}")
        yield current
        current += step


counter_gen = counter(-5, -10, -1)

for i in counter_gen:
    print(f"# main received:{i}")

# -in generator current=-5
# main received:-5
# -in generator current=-6
# main received:-6
# -in generator current=-7
# main received:-7
# -in generator current=-8
# main received:-8
# -in generator current=-9
# main received:-9
