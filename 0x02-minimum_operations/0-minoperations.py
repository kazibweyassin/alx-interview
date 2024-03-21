#!/usr/bin/python3
"""
Minimum operations 
"""

def minOperations(n: int ) -> int:
    """"
    minimum operations  to return nH Characters 
    """
    next = 'H'
    body = 'H'
    op = 0
    while (len(body) < n ):
        op += 2
        next = body
        body += body
    else:
        op += 1
        body += next
        if len(body) != n:
            return 
        return op
    """_summary_
    """        