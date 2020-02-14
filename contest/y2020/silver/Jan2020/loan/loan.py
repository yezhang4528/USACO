import bdb
import sys

if len(sys.argv) > 1:
    inputFile = "data/%s.in" % sys.argv[1]
else:
    inputFile = "loan.in"

with open(inputFile, "r") as fin:
    N, K, M = map(int, fin.readline().split())

#print(N, K, M)
def satisfyProc(x):
    g = 0
    n = N
    k = K
    m = M

    while k > 0 and g < n:
        y = (n - g) // x
        if (y < m):
            leftover = (n - g + m - 1) // m
            return leftover <= k
        maxmatch = n - x*y
        numdays = (maxmatch - g) // y
        if numdays > k:
            numdays = k
        elif numdays == 0:
            numdays = 1
        g += y * numdays
        k -= numdays
    return g >= n

def getMaxX(lower, upper):
    if lower >= upper:
        return lower

    if lower == upper - 1:
        if satisfyProc(upper):
            return upper
        else:
            return lower

    mid = (lower + upper) // 2
    if satisfyProc(mid):
        return getMaxX(mid, upper)
    else:
        return getMaxX(lower, mid-1)
try:
    #import pdb; pdb.set_trace()    # sarah, for debugging
    X = getMaxX(1, N//M)
except Exception as e:
    if isinstance(e, bdb.BdbQuit):
        exit(0)

with open("loan.out", "w") as fout:
    fout.write(str(X) + '\n')
