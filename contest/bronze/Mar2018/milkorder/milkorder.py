'''
Create CowDict, key is position, starting from 1->N, value is cowNum, initialize to 0.
Read and insert all special order cows into CowDict, if cowNum == 1, return position
Reversly traverse the hierOrder cow List. Declare InsertIndex, initialize to last
    1: If cow is in CowDict, update InsertIndex to position (Cows in hierOrder list should be in front of this cow)
    2: If Cow is not in CowDict. Insert cow to the last empty spot before InsertIndex, update InsertIndex
        * If cow is 1, mark cow1Position (Init to 0)
    3. Repeat 2 until cow is in CowDict
        * If cow1Position == 0, update InsertIndex
        * If cow1Position != 0
            * If insert position == CowDict, return cow1Position
            * If insert position > CowDict position, return cow1Position - diff
    4. Reach 1st cow in hierOrder List.
        * If cow1Position == 0, return 1st empty spot position in CowDict
        * If cow1Position != 0, return cow1Position - (InsertIndex - 1)
'''
def insertSpecialOrderCows(specialPosLines, posToCowDict, cowToPosDict):
    for line in specialPosLines:
        cow, pos = map(int, line.split())
        posToCowDict[pos] = cow
        cowToPosDict[cow] = pos
        # Check whether it's cow 1, if true, return position, end
        if posToCowDict[pos] == 1:
            return pos
    return 0

def findEmpty(posToCowDict, insertIndex):
    for index in range(insertIndex, 0, -1):
        if posToCowDict[index] == 0:
            return index
    return 0

def getFirstEmptySlot(posToCowDict, startIndex):
    for i in range(startIndex, len(posToCowDict) + 1):
        if posToCowDict[i] == 0:
            return i
    return 0

def insertFromBeginning(posToCowDict, cowToPosDict, hierList):
    cow1pos = 0
    insertIndex = 1
    for i in range(0, len(hierList)):
        cow = hierList[i]
        if cow in cowToPosDict:
            insertIndex = cowToPosDict[cow]
            continue
        pos = getFirstEmptySlot(posToCowDict, insertIndex)
        posToCowDict[pos] = cow
        cowToPosDict[cow] = pos
        if cow == 1:
            cow1pos = pos
            break
    return cow1pos

def insertHierOrderCows(hierCowList, posToCowDict, cowToPosDict):
    cow1Pos = 0
    if 1 in hierCowList:
        cow1Pos = insertFromBeginning(posToCowDict, cowToPosDict, hierCowList)
        return cow1Pos

    # if cow 1 is not in hierCowList, after inserting all hier cows, find the first empty slot
    insertIndex = len(posToCowDict)
    hierIndex = len(hierCowList) - 1
    while hierIndex >= 0:
        # The cow already got inserted into the list (key exist in cowToPosDict).
        newCow = hierCowList[hierIndex]
        if newCow in cowToPosDict:
            insertIndex = cowToPosDict[newCow]
        else:
            # the cow is not inserted yet, insert it
            emptySpot = findEmpty(posToCowDict, insertIndex)
            if emptySpot != 0:
                posToCowDict[emptySpot] = newCow
                cowToPosDict[newCow] = emptySpot
                insertIndex = emptySpot - 1
            else:
                print("emptySpot == 0")
        hierIndex -= 1
    cow1Pos = getFirstEmptySlot(posToCowDict, 1)
    return cow1Pos

with open("milkorder.in", "r") as fin:
    cowNumLine = fin.readline()
    hierLine = fin.readline()
    specialPosLines = fin.readlines()

totalCow, hierCows, specialPosCows = map(int, cowNumLine.split())
# cowDict: key is cow position from 1->N, value is cow, init all values to 0
posToCowDict = {}
cowToPosDict = {}
for i in range(1, totalCow + 1):
    posToCowDict[i] = 0

fout = open("milkorder.out", "w")
cow1Position = 0
# Insert special order cow into cowDict. If cow 1 is in, write cow1 position
cow1Position = insertSpecialOrderCows(specialPosLines, posToCowDict, cowToPosDict)
if cow1Position == 0:
    hierCowList = list(map(int, hierLine.split()))
    cow1Position = insertHierOrderCows(hierCowList, posToCowDict, cowToPosDict)

fout.write(str(cow1Position))

fout.close()
