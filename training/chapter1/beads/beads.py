'''
ID: yezhang2
LANG: PYTHON3
TASK: beads
'''

'''
Concatnate the beads head and tail
Case 1:
wwwbbrwrbrbrrbrbrwrwwrbwrwrrb | wwwbbrwrbrbrrbrbrwrwwrbwrwrrb
Replace w to the sure color, meaning replace w if left and right neighbor are same color

wwwbbrrrbrbrrbrbrrrrrrbwrrrrb | wwwbbrrrbrbrrbrbrrrrrrbwrrrrb

w  b r  brbr brbr     bwr   b | w  b r  brbr brbr     bwr   b
3  2 3  1112 1116     114   1 | 3  2 3  1112 1116     114   1

wbrbrbrbrbrbwrbwbrbrbrbrbrbwrb
323111211161141323111211161141

Unify string by inserting w
wbwrwbwrwbwrwbwrwbwrwbwrwbwbwr...
320301010102010101060114010302...

Eliminate the w and add 1 to the larger neighbor (This won't work, reason is same as replacing w with color forward and backward. It depends the right 2 neighbors
brbrbrbrbrbrbrbrbrbrbrbrb
5311121116156311121116151

Find the biggest 2 neighbor, that's the answer we are looking for.

Case 2:
Whole string contains the same color beads, with/without replacing 'w'

Example why concatenate works.

rrrrb | rrrrb

rrrrbrrrrb (The concatenate string definitely contains the longest result)
'''
# Read input.


def replaceW(beadLine, curIndex, curColor):
    numReplaced = 0
    for i in range(curIndex, len(beadLine)):
        if beadLine[i] == 'w':
            beadLine[i] = curColor
            numReplaced += 1
        else:
            break
    return numReplaced

def findNextColor(beadLine, index):
    for i in range(index, len(beadLine)):
        if beadLine[i] != 'w':
            return beadLine[i] 
    return ''

# Replace 'w' if both sides are the same color
def replaceSureW(beadLine):
    curColor = ''
    i = 0
    while i < len(beadLine):
        if curColor == '' and beadLine[i] == 'w':
            i += 1
            continue

        if beadLine[i] != 'w':
            curColor = beadLine[i]
            i += 1
            continue

        if beadLine[i] == 'w':
            nextColor = findNextColor(beadLine, i)
            if curColor == nextColor:
                n = replaceW(beadLine, i, curColor)
                i += n
            else:
                i += 1
    return beadLine
    
def insertW(beadLine, beadList, beadCount):
    listIndex = 0
    for x in beadLine:
        if len(beadList) != 0 and x == beadList[listIndex-1]:
            beadCount[listIndex-1] += 1
        else:
            if len(beadList) != 0 and x != 'w' and beadList[listIndex-1] != 'w':
                beadList.append('w')
                beadCount.append(0)
                listIndex += 1
            beadList.append(x)
            beadCount.append(1)
            listIndex += 1

def countMax(beadList, beadCount):
    i = 0
    maxCollect = 0
    if len(beadList) <= 4:
       for x in beadCount:
           maxCollect += x
       return maxCollect

    if beadList[i] != 'w':
        maxCollect = beadCount[i] + beadCount[i+1] + beadCount[i+2] + beadCount[i+3]
        i += 1
    while i < len(beadList) - 4:
        tempMax = beadCount[i] + beadCount[i+1] + beadCount[i+2] + beadCount[i+3] + beadCount[i+4]
        if maxCollect < tempMax:
            maxCollect = tempMax
        i += 2
    return maxCollect

with open("beads.in", "r") as fin:
    totalBeads = int(fin.readline())
    beadSeq = list(fin.readline().strip('\n'))

beadUnified = []
unifiedCount = []
insertW(beadSeq, beadUnified, unifiedCount)

maxCollect = 0
if len(beadUnified) <= 3:
    maxCollect = len(beadSeq)
else:
    beadSeq.extend(beadSeq)
    bead1stRound = replaceSureW(beadSeq)
    beadUnified = []
    unifiedCount = []
    insertW(bead1stRound, beadUnified, unifiedCount)
    maxCollect = countMax(beadUnified, unifiedCount)

with open("beads.out", "w") as fout:
    fout.write(str(maxCollect) + '\n')
