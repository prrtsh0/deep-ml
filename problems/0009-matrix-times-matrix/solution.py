def matrixmul(a: list[list[int|float]],
              b: list[list[int|float]]) -> list[list[int|float]]:
    # (m x n) @ (n x p) only works if cols of a == rows of b
    if not a or not b or len(a[0]) != len(b):
        return -1

    m, n, p = len(a), len(a[0]), len(b[0])
    c = [[0] * p for _ in range(m)]

    for i in range(m):
        for j in range(p):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    return c