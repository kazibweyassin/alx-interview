#!/usr/bin/python3
""""Minimum operationserations """

def minoperationserations(n: int ) -> int:
    """"minimum operationserations  to return nH Characters """
    next = 'H'
    body = 'H'
    operations = 0
    while (len(body) < n ):
        operations += 2
        next = body
        body += body
    else:
        operations += 1
        body += next
        if len(body) != n:
            return 0
        return operations
        