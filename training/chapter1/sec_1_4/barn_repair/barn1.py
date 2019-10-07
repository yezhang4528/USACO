'''
ID: yezhang2
LANG: PYTHON3
TASK: barn1
'''
'''
Giving cow list (by index), having 4 boards meaning we'll separate the cows into 4 groups,
with 3 split points, the disstance between at this 3 points should be maximum of all.

Example: number -- a cow, x -- empty
3 4 x 6 x 8 x x x x x 14 15 16 17 x x x 21 x x x 25 26 27 x x 30 31 x x x x x x x x 40 41 42 43
    1   1       5                   3        3             2                8

Meaning we should split cows at max distance 8, 5 and 3,
In this function, we'll return list of pairs (index, distance)

NOTE: corner cases:
1. There is only one board
2. Board number > total cow
3. 
NOTE: Maximum total boards might be greater than the split pairs, then all pairs can be used
'''
def getSplitPair(cowList, totalGroups):
    indexDistPairList = []
    pos = 0
    distance = 0
    for i in range(cowList[0], cowList[-1]+ 1):
        if i == cowList[pos]:
            pos = pos + 1
            if distance > 0:
                indexDistPairList.append((distance, (i-distance)))
                distance = 0
            continue
        else:
            distance = distance + 1
    # sort list by distance, get the max distance pairs
    sortedList = sorted(indexDistPairList, key = lambda x:x[0])

    # split number = totalGroups - 1, that's the number of pairs returns
    if len(sortedList) <= totalGroups - 1:
        return sortedList
    else:
        return sortedList[-(totalGroups-1):]

def calculateBlocked(sortedIndexList, cowList):
    maxRange = cowList[-1] - cowList[0] + 1
    skipped = 0
    for pair in sortedIndexList:
        skipped = skipped + pair[0]
    return (maxRange - skipped)
            
cowIndexList = []
with open("barn1.in", "r") as fin:
    maxBoards, totalStalls, totalCow = map(int, fin.readline().split())
    lines = fin.read().split('\n')
    for line in lines:
        if len(line) > 0:
            cowIndexList.append(int(line))

totalMinBlocked = 0
sortedCowList = sorted(cowIndexList)
if maxBoards == 1:
    totalMinBlocked = sortedCowList[-1] - sortedCowList[0] + 1
elif maxBoards >= totalCow:
    totalMinBlocked = totalCow
else:
    splitPairList = getSplitPair(sortedCowList, maxBoards)
    # sort return list by index
    sortedIndexList = sorted(splitPairList, key = lambda x:x[1])
    totalMinBlocked = calculateBlocked(sortedIndexList, sortedCowList)
    
with open("barn1.out", "w") as fout:
    fout.write(str(totalMinBlocked) + '\n')
