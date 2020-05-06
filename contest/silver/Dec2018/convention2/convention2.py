import bdb
import sys
from heapq import heappush, heappop, heapify

cows = []
if len(sys.argv) > 1:
    inputFile = "data/%s.in" % sys.argv[1]
else:
    inputFile = "convention2.in"

with open(inputFile, "r") as fin:
    totalCows = int(fin.readline().strip())
    for i in range(totalCows):
        arr, graze = map(int, fin.readline().split())
        cows.append((i, arr, graze))

cows.sort(key=lambda x: x[1])
#print(cows)
maxWait = 0
cowInQ = []
pWait = cows[0][2] + cows[0][1]       # pasture pending time

def processQ(cows):
    global pWait, maxWait
    cow = heappop(cows)
    wait = pWait - cow[1]
    maxWait = max(maxWait, wait)
    pWait = pWait + cow[2]

try:
    #import pdb; pdb.set_trace()     # sarah, for debugging
    heapify(cowInQ)
    for cow in cows[1:]:
        if pWait <= cow[1] and len(cowInQ) == 0:
            # no wait
            pWait = cow[1] + cow[2]
            continue
    
        # Pasture will be available before the cow arrives.
        # Process cows in Q.
        while pWait < cow[1] and len(cowInQ) > 0:
            processQ(cowInQ)
    
        if pWait >= cow[1]:
            heappush(cowInQ, cow)
        else:
            # no wait
            pWait = cow[1] + cow[2]

    while len(cowInQ) > 0:
        processQ(cowInQ)

except Exception as e:
    if isinstance(e, bdb.BdbQuit):
        exit(0)

with open("convention2.out", "w") as fout:
    fout.write(str(maxWait) + '\n')
