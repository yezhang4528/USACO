'''
ID: yezhang2
LANG: PYTHON3
TASK: milk2
'''
'''
Readinput, make list of paird time. sort list by first element (start time)
Since the list is sorted, only following scenarios need to be handled.
* The new pair is fully overlapped/covered by old pair. In this case, do nothing, and leave the compared one not changed (do not update to new pair)
* The new pair intersects with old pair, update longestMilk time to include the extended distance introduced by new pair. Update compare pair to the extended pair (start, newStop)
* The new pair doesn't have any overlap with old pair. Calculate new no milk time, newStart - stop. Compare with longestNoMilk time, save the bigger one. Update compare pair with new pair.
'''
longestMilk = longestNoMilk = 0

def getLongest(comparePair, newPair):
    global longestMilk, longestNoMilk

    newStart = newPair[0]
    newStop = newPair[1]
    start = comparePair[0]
    stop = comparePair[1]
    #print(start, stop, newStart, newStop)
    newToCompare = []
    if newStart <= stop and stop < newStop:
        newdiff = newStop - stop + (stop - start)
        longestMilk = max(longestMilk, newdiff)
        newToCompare.append(start)
        newToCompare.append(newStop)
    elif stop < newStart:
        longestNoMilk = max(longestNoMilk, (newStart - stop))
        newToCompare = newPair
    else:
        #if newStop < stop, the case is ignored.
        newToCompare = comparePair

    #print(longestMilk, longestNoMilk)
    return newToCompare

milkPairList = []
with open("milk2.in", "r") as fin:
    cows = int(fin.readline())
    lines = fin.readlines()
    for line in lines:
        newList = list(map(int, line.split()))
        milkPairList.append(newList)

milkPairList.sort()
#print(milkPairList)
comparePair = milkPairList[0]
longestMilk = comparePair[1] - comparePair[0]
for i in range(1, len(milkPairList)):
    comparePair = getLongest(comparePair, milkPairList[i])

#print(longestMilk)
#print(longestNoMilk)

with open("milk2.out", "w") as fout:
    fout.write(str(longestMilk) + " " + str(longestNoMilk) + "\n")
