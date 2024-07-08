"""Module 1 for demoing namespace
"""
"""Here is the global namespace of module 1
The following objects exist in this namespace:
Functions:
    M1FA
Constant:
    M1CONST
"""

M1CONST = "CONSTANT in Module 1"

def M1FA(msg: str = '') -> None:
    """Function A of module 1
    Args:
        msg: the message sent from the caller

    Returns:
        None
    """
    """Here is the M1FA local namespace
    The following objects exist in this namespace:
    Functions:
        M1FA1
    Parameters:
        msg
    Variables:
        stack_depth
    """
    stack_depth = msg.count("<-")
    def M1FA1(msg: str = '') -> None:
        """Sub Function A1 of of module 1
        """
        """Here is the M1FA1 local namespace
        The following objects exist in this namespace:
        Parameters:
            msg (shadowed)
        Vaiables:
            stack_depth (shadowed)
        """
        stack_depth = msg.count("<-")
        print(f"# {' '*stack_depth}in M1FA1, {M1CONST=}, {msg}.")

    print(f"# {' '*stack_depth}entering M1FA, {msg}...")
    M1FA1(f"<-from M1FA{msg}")
    print(f"# {' '*stack_depth}exiting M1FA, {msg}.")
