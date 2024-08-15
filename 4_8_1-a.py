from collections.abc import Generator


def counter() -> Generator[int]:
    """Demo generator function.

    Yields:
        sequence number starts from 1 ends at 3.
    """
    print(f"# generator yielding the first...")
    yield 1
    print(f"# generator yielding the second...")
    yield 2
    print(f"# generator yielding the third...")
    yield 3


seq_nos = counter()
print(f"#seq_nos is a {type(seq_nos)}")
# seq_nos is a <class 'generator'>

for seq_no in seq_nos:
    print(f"#main received:{seq_no}")
# generator yielding the first...
# main received:1
# generator yielding the second...
# main received:2
# generator yielding the third...
# main received:3
[]
