"""Module demo global/local scope of module import

A module contain global var and function that can be invoked from 
within the program import this module.
"""
"""save this as m6_2_scope.py"""

global_var = 'value set in m6_2_scope'

def check_global_var() -> str:
    """return the value of global_var
    
    Returns:
        string value of global_var
    """
    return global_var

def len(anything: any) -> str:
    """return stringified value with prefix LEN
    
    Args:
        any object that can be converted to str.
        
    Returns:
        LEN+str(any)
    """
    return 'LEN'+str(anything)
