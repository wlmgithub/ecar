
import sys
N = sys.argv[1]
N = int(N)

def pascal(n):
    res = [ [1] * (i + 1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            res[i][j] = res[i-1][j-1] + res[i-1][j]
    return res


res = pascal(N)
for i in res:
    print(i)
