"""
1. Two barns at postion 0, L (left, right)
2. Sort all cows by position (left to right)
3. Fact 1: Regardless bouncing, if there is n cows moving right (velocity 1),
   there will be n cows ended in right barn.
   Therefore, for m cows moving left (velocity -1), there will be m cows ended in left barn.
4. Fact 2: After sorting, all left most n cows will be ended at left barn, regardless its velocity.
   All right most m cows will be ended at right barn, regardless its velocity.
5. Fact 3: To calculate each cow traveling time, based on each cow's initial position and velocity,
   we can get each cow's travel to barn's time, and assign them corresponding to the left/right position.
6. Then we'll get total weight reaching the barn, and stop when either one reaches half weight.
7. Calculate meeting time: 
   Scan through the list, queue all cows heading to right barn, compare with the cows heading left,
   as long as the position and stopTime(T) satisfy following condition, the cows will meet.
   Xi + T >= Xj - T (Xi: moving right, Xj: moving left, after time T, Xi is the same position or
                     right side of Xj, they will meet)
   => Xi + 2T >= Xj

Example:
   Barn position 0, 5,
   Total cows: 3
            Xi      Weight      Velocity
   Cow 1:   1       1           1 
   Cow 2:   2       2           -1
   Cow 3:   3       3           -1 

In the end, there will be 2 cows reaching left barn, and one cow reaching right barn.
The cows reaching left barn will be cow1 and cow2 (based on their X coordination)
Cow 3 will reach right barn.

To calcuate cow1 and cow2 travel to left-barn time, use cow2 and cow3 position.
Cow1 : 2 time unit
Cow2 : 3 time unit

Cow3 reaching right-barn time is based on cow1 position.
Cow3 : 4 time unit

End point: When cow 2 reaches left barn, cow1Weight + cow2Weight > half of total weight.


Search original cow list with velocity, and compare with cow destination, If the cow's
velocity is different from its end point, there is meeting.

Special case:
    Only one velocity,

"""
import bdb
import sys

def calculateStopTime(cowInOrder, lTimeList, rTimeList, stopWeight):
    lTimeList.sort()
    rTimeList.sort(reverse=True)
    print(lTimeList)
    print(rTimeList)
    wInBarn = 0
    lTimeLen = len(lTimeList)
    rTimeLen = len(rTimeList)
    i = 0
    j = rTimeLen - 1
    cowIndex = 0
    stopTime = 0
    while i < lTimeLen and j >= 0:
        if lTimeList[i] < rTimeList[j]:
            wInBarn += cowInOrder[i][0]
            stopTime = lTimeList[i]
            i += 1
        else:
            cowIndex = lTimeLen + j
            wInBarn += cowInOrder[cowIndex][0]
            stopTime = rTimeList[j]
            j -= 1
        if wInBarn >= stopWeight:
            return stopTime
  
    while i < lTimeLen:
        wInBarn += cowInOrder[i][0]
        stopTime = lTimeList[i]
        if wInBarn >= stopWeight:
            return stopTime
        i += 1
    while j > 0:
        cowIndex = lTimeLen + j
        wInBarn += cowInOrder[cowIndex][0]
        stopTime = rTimeList[j]
        if wInBarn >= stopWeight:
            return stopTime
        j -= 1
    return stopTime

def getMeeting(cowInOrder, T):
    meeting = 0
    twoT = 2 * T
    cowInRange = []
    for cow in cowInOrder:
        if cow[2] == -1:
            if len(cowInRange) > 0:
                deleteRange = 0
                while deleteRange < len(cowInRange) and cowInRange[deleteRange][1] + twoT < cow[1]:
                    deleteRange += 1
                if deleteRange > 0:
                    del(cowInRange[0:deleteRange])
                meeting += len(cowInRange)
        else:   # velocity == 1, move to right
            cowInRange.append(cow)

    return meeting

cowList = []
cowToLeft = 0
cowToRight = 0
meetings = 0
lTimeList = []
rTimeList = []
totalWeight = 0
#with open("meetings.in", "r") as fin:
inputFile = "data/%s.in" % sys.argv[1]
print(inputFile)
with open(inputFile, "r") as fin:
    totalCows, right = map(int, fin.readline().split())
    #print(totalCows, right)
    for i in range(totalCows):
        weight, x, velocity = map(int, fin.readline().split())
        totalWeight += weight
        cowList.append((weight, x, velocity))
        if velocity == 1:
            cowToRight += 1
            rTimeList.append(right - x)
        else:
            cowToLeft += 1
            lTimeList.append(x)

try:
    if cowToRight == 0 or cowToLeft == 0:
        meetings = 0
    else:
        cowInOrder = sorted(cowList, key=lambda x: x[1])
        #import pdb; pdb.set_trace()        # sarah: Uncomment to debug
        T = calculateStopTime(cowInOrder, lTimeList, rTimeList, totalWeight/2)
        # calculate meeting time
        print("Stop Time %d" % T)
        meetings = getMeeting(cowInOrder, T)

except Exception as e:
    if isinstance(e, bdb.BdbQuit):
        # Could be caused by pdb quit, no need to raise and/or handle the exception
        sys.exit(0)


with open("meetings.out", "w") as fout:
    fout.write(str(meetings) + '\n')
