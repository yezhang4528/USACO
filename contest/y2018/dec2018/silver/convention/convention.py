"""
1. Step 1: Start binary search, range from 0 - 10^9. If the optimal Max waiting time is satisfied with the mid, search lower, otherwise search higher.

2. For each Max waiting time passed in, run through entire list to see with this Max waiting time, whether all the cows can be shipped by the buses.
   if yes, continue to search lower, this is a candidate for the Max waiting time.

import bdb
num = sys.argv[1]
inputFile = "data/%s.in" % num
with open(inputFile, "r") as fin:
"""

import sys
with open("convention.in", "r") as fin:
    totalCows, buses, C = map(int, fin.readline().split())
    tList = list(map(int, fin.readline().split()))

tList.sort()

def canShip(waitT):
    global tList, totalCows, buses, C
    #if waitT == 103292:                    # sarah: Should be can't ship
    #    import pdb; pdb.set_trace()        # sarah: Uncomment to debug
    busNeed = 1
    firstCowT = tList[0]       # Time that first cow gets on this bus.
    leftRoom = C - 1
    for t in tList[1:]:
        if t - firstCowT > waitT or leftRoom == 0:
            busNeed += 1
            firstCowT = t
            leftRoom = C - 1
        else:
            leftRoom -= 1
    return (busNeed <= buses)

def getOptimalMax(low, high):
    global tList, totalCows, buses, C
    #print (totalCows, buses, C)
    #print(tList)
    if low >= high:
        if canShip(low):
            return low
        else:
            return -1
    mid = (low + high) // 2
    if canShip(mid):
        opMax = getOptimalMax(low, mid - 1)
        if opMax != -1:
            return opMax
        else:
            return mid
    else:
        return getOptimalMax(mid + 1, high)

# cow i arrives at time ti (0 <= ti <= 10^9).
try:
    #import pdb; pdb.set_trace()        # sarah: Uncomment to debug
    optimalMax = getOptimalMax(0, 1000000000)
except Exception as e:
    if isinstance(e, bdb.BdbQuit):
        # Could be caused by pdb quit, no need to raise and/or handle the exception
        sys.exit(0)

#print(optimalMax)
with open("convention.out", "w") as fout:
    fout.write(str(optimalMax) + '\n')
