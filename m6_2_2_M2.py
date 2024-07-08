"""Module 2 for demoing namespace
"""
"""Here is the global namespace of module 2
The following objects exist in this namespace:
Functions:
    M2FA
    M2FB
Variables:
    m2var
"""

m2var = "variable in Module 2"

def M2FA(msg: str = '') -> None:
    """Function A of module 2
    Args:
        msg: the message sent from the caller

    Returns:
        None
    """
    """Here is the M2FA local namespace
    The following objects exist in this namespace:
    Functions:
        M2FA1
        M2FA2
    Parameters:
        msg
    Variables:
        stack_depth
    """
    stack_depth = msg.count("<-")
    def M2FA1(msg: str = '', stack_depth: int = 0) -> None:
        """Sub Function A1 of of module 2
        """
        """Here is the M2FA1 local namespace
        The following objects exist in this namespace:
        Parameters:
            msg (shadowed)
        Variables:
            stack_depth (shadowed)
        """
        stack_depth = msg.count("<-")
        print(f"# {' '*stack_depth}in M2FA1, {m2var=}, {msg}.")

    def M2FA2(msg: str = '', stack_depth: int = 0) -> None:
        """Sub Function A2 of of module 2
        """
        """Here is the M2FA2 local namespace
        The following objects exist in this namespace:
        Parameters:
            msg (shadowed)
        Variables:
            stack_depth (shadowed)
        """
        stack_depth = msg.count("<-")
        print(f"# {' '*stack_depth}in M2FA2, {m2var=}, {msg}.")

    print(f"# {' '*stack_depth}entering M2FA, {msg}...")
    M2FA1(f"<-from M2FA{msg}")
    M2FA2(f"<-from M2FA{msg}")
    if "M2FB" not in msg:
        M2FB(f"<-from M2FA{msg}")
    print(f"# {' '*stack_depth}exiting M2FA, {msg}.")
    
def M2FB(msg: str = '') -> None:
    """Function B of module 2
    Args:
        msg: the message sent from the caller

    Returns:
        None
    """
    """Here is the M2FB local namespace
    The following objects exist in this namespace:
    Functions:
        M2FB1
    Parameters:
        msg (shadowed)
    Variables:
        stack_depth (shadowed)
    """
    stack_depth = msg.count("<-")
    def M2FB1(msg: str = '') -> None:
        """Sub Function B1 of of module 2
        """
        """Here is the M2FB1 local namespace
        The following objects exist in this namespace:
        Parameters:
            msg (shadowed)
        Variables:
            stack_depth (shadowed)
        """
        stack_depth = msg.count("<-")
        print(f"# {' '*stack_depth}in M2FB1, {msg}.")

    print(f"# {' '*stack_depth}entering M2FB, {msg}...")
    M2FB1(f"<-from M2FB{msg}")
    if "M2FA" not in msg:
        M2FA(f"<-from M2FB{msg}")
    print(f"# {' '*stack_depth}exiting M2FB, {msg}.")
