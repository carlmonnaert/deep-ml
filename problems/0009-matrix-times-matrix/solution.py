import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    n,m = len(a), len(a[0])
    k,l = len(b), len(b[0])
    if m != k:
        return -1
    
    c = [ [sum([ a[i][p] * b[p][j] for p in range(k)]) for j in range(l)] for i in range(n)]
    return c