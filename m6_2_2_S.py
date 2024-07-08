"""main script for demoing namespace
"""
"""Here is the global namespace of this script
The following objects exist in this global namespace:
Functions:
    SFA
    SFB
Modules:
    M1
    M2
"""

import m6_2_2_M1 as M1
import m6_2_2_M2 as M2

def SFA(msg: str = '') -> None:
    """Function A of main script
    Args:
        msg: the message sent from the caller
    Returns:
        None
    """
    """Here is the SFA local namespace
    The following objects exist in this namespace:
    Modules:
        M1
        M2
    Functions:
        SFA1
        SFA2
    Parameters:
        msg
    Variables:
        stack_depth
    """
    stack_depth = msg.count("<-")
    def SFA1(msg: str = '') -> None:
        """Sub Function A1 of main script
        """
        """Here is the SFA1 local namespace
        The following objects exist in this namespace:
        Parameters:
            msg  (shadowed)
        Vaiable:
            stack_depth (shadowed)
        """
        stack_depth = msg.count("<-")
        print(f"# {' '*stack_depth}entering SFA1, {msg}...")
        M1.M1FA(f"<-from SFA1{msg}")
        print(f"# {' '*stack_depth}exiting SFA1, {msg}.")

    def SFA2(msg: str = '') -> None:
        """Sub Function A2 of main script
        """
        """Here is the SFA2 local namespace
        The following objects exist in this namespace:
        Parameters:
            msg (shadowed)
        Variables:
            stack_depth (shadowed)
        """
        stack_depth = msg.count("<-")
        print(f"# {' '*stack_depth}entering SFA2, {msg}...")
        M2.M2FB(f"<-from SFA2{msg}")
        print(f"# {' '*stack_depth}exiting SFA2, {msg}.")
    print(f"# {' '*stack_depth}entering SFA, {msg}...")
    SFA1(f"<-from SFA{msg}")
    SFA2(f"<-from SFA{msg}")
    if "SFB" not in msg:
        SFB(f"<-cfrom SFB{msg}")
    print(f"# {' '*stack_depth}exiting SFA, {msg}.")

def SFB(msg: str = '') -> None:
    """Function B of main script
    Args:
        msg: the message sent from the caller

    Returns:
        None
    """
    """Here is the SFB local namespace
    The following objects exist in this namespace:
    Functions:
        SFB1
    Parameters:
        msg (shadowed)
    Variables:
        stack_depth (shadowed)
    """
    stack_depth = msg.count("<-")
    def SFB1(msg: str = '') -> None:
        """Sub Function B1 of main script
        """
        """Here is the SFB1 local namespace
        The following objects exist in this namespace:
        Parameters:
            msg (shadowed)
        Variables:
            stack_depth (shadowed)
        """
        stack_depth = msg.count("<-")
        print(f"# {' '*stack_depth}entering SFB1, {msg}...")
        M2.M2FA(f"<-from SFB1{msg}")
        print(f"# {' '*stack_depth}exiting SFB1, {msg}.")

    print(f"# {' '*stack_depth}entering SFB, {msg}...")
    SFB1(f"<-from SFB{msg}")
    if "SFA" not in msg:
        SFA(f"<-from SFB{msg}")
    print(f"# {' '*stack_depth}exiting SFB, {msg}.")


SFB(" <-from main script")
#  entering SFB,  <-from main script...
#   entering SFB1, <-from SFB <-from main script...
#    entering M2FA, <-from SFB1<-from SFB <-from main script...
#     in M2FA1, m2var='variable in Module 2', <-from M2FA<-from SFB1<-from SFB <-from main script.
#     in M2FA2, m2var='variable in Module 2', <-from M2FA<-from SFB1<-from SFB <-from main script.
#     entering M2FB, <-from M2FA<-from SFB1<-from SFB <-from main script...
#      in M2FB1, <-from M2FB<-from M2FA<-from SFB1<-from SFB <-from main script.
#     exiting M2FB, <-from M2FA<-from SFB1<-from SFB <-from main script.
#    exiting M2FA, <-from SFB1<-from SFB <-from main script.
#   exiting SFB1, <-from SFB <-from main script.
#   entering SFA, <-from SFB <-from main script...
#    entering SFA1, <-from SFA<-from SFB <-from main script...
#     entering M1FA, <-from SFA1<-from SFA<-from SFB <-from main script...
#      in M1FA1, M1CONST='CONSTANT in Module 1', <-from M1FA<-from SFA1<-from SFA<-from SFB <-from main script.
#     exiting M1FA, <-from SFA1<-from SFA<-from SFB <-from main script.
#    exiting SFA1, <-from SFA<-from SFB <-from main script.
#    entering SFA2, <-from SFA<-from SFB <-from main script...
#     entering M2FB, <-from SFA2<-from SFA<-from SFB <-from main script...
#      in M2FB1, <-from M2FB<-from SFA2<-from SFA<-from SFB <-from main script.
#      entering M2FA, <-from M2FB<-from SFA2<-from SFA<-from SFB <-from main script...
#       in M2FA1, m2var='variable in Module 2', <-from M2FA<-from M2FB<-from SFA2<-from SFA<-from SFB <-from main script.
#       in M2FA2, m2var='variable in Module 2', <-from M2FA<-from M2FB<-from SFA2<-from SFA<-from SFB <-from main script.
#      exiting M2FA, <-from M2FB<-from SFA2<-from SFA<-from SFB <-from main script.
#     exiting M2FB, <-from SFA2<-from SFA<-from SFB <-from main script.
#    exiting SFA2, <-from SFA<-from SFB <-from main script.
#   exiting SFA, <-from SFB <-from main script.
#  exiting SFB,  <-from main script.
