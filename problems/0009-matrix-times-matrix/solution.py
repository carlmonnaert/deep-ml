def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if len(a[0]) != len(b):
        return -1
    n = len(a)
    m = len(b[0])
    r = len(b) 
    return[[sum([a[i][k] * b[k][j] for k in range(r)]) for j in range(m)] for i in range(n)]