'''
ID: yezhang2
LANG: PYTHON3
TASK: skidesign
'''
'''
* Read in input data, sort.
* Calculate diff between 2 points, starting point is sortList head, ending point is sortList tail
* Then to second to sortList head, and second to sortlist tail, ..., and so on.
* If diff is greater than 17, add to toBeCaculatedList, eliminate the rest. End of adding toBeCalculatedList.
* Define lowMark and highMark. lowMark is the first element of the sort list. If above diff is equal to 17,
* highMark is the smaller number(starting point), otherwise highMark = previous ending point - 17
* Define scale list of pairs. 1st element: lowMark to hightMark. 2nd element: 1st element + 17
* For each pair, calculate cost for all toBeCalculatedList, save the minimum one.
*
* Example:
* Input after sorted: 1 4 20 21 24
* toBeCalculatedList = [1, 24]
* lowMark: 1; highMark 4
* List of pairs: [(1, 18), (2, 19), (3, 20), (4, 21)]
* Calculate cost:
* (1, 18): (1-1)^2 + (24-18)^2 = 36
* (2, 19): (2-1)^2 + (24-19)^2 = 1 + 25 = 26
* (3, 20): (3-1)^2 + (24-20)^2 = 4 + 16 = 20
* (4, 21): (4-1)^2 + (24-21)^2 = 9 + 9 = 18
* Therefore, answer is 18

'''
hills = []

with open("skidesign.in", "r") as fin:
    totalHills = int(fin.readline())
    for i in range(0, totalHills):
        hills.append(int(fin.readline()))

sortedHills = sorted(hills)
#print(sortedHills)
#print("Length of sortedHills: %d" % len(sortedHills))

def prepareScaleList(lowMark, highMark):
    scalePairList = []
    if lowMark == highMark:
        return scalePairList

    for i in range(lowMark, highMark + 1):
        scalePair = (i, i+17)
        scalePairList.append(scalePair)
    return scalePairList

getMin = lambda x, scale1, scale2: min(abs(x-scale1), abs(x-scale2))
def calculateFinalCost(scaleList, list1, list2):
    finalCost = 0
    for scalePair in scaleList:
        cost = 0
        for i in range(0, len(list1)):
            diff1 = getMin(list1[i], scalePair[0], scalePair[1])
            diff2 = getMin(list2[i], scalePair[0], scalePair[1])
            cost += diff1**2
            cost += diff2**2
            '''
            if scalePair[0] == 43:
                print("diff1: %d" % diff1, "diff2: %d" % diff2)
                print("cost: %d" % cost)
            '''

        if finalCost == 0:
            finalCost = cost

        if finalCost > cost:
            finalCost = cost
    return finalCost

changeList1 = []
changeList2 = []

fwdIndex = 0
bckIndex = len(sortedHills) - 1
highMark = 0
while True:
    if sortedHills[bckIndex] - sortedHills[fwdIndex] < 17:
        if bckIndex == len(sortedHills) - 1:    # no need to do any modification
            highMark = sortedHills[fwdIndex]
        else:
            highMark = sortedHills[bckIndex + 1] - 17
        break

    if sortedHills[bckIndex] - sortedHills[fwdIndex] == 17:
        highMark = sortedHills[fwdIndex]
        break

    changeList1.append(sortedHills[fwdIndex])
    changeList2.append(sortedHills[bckIndex])
    fwdIndex += 1
    bckIndex -= 1
    if fwdIndex >= bckIndex:
       highMark = sortedHills[bckIndex + 1] - 17
       break

sum1 = 0
sum2 = 0
for i in range(0, len(changeList1)):
    sum1 += changeList1[i]
    sum2 += changeList2[i]

scaleList = prepareScaleList(sum1//len(changeList1), highMark)
#print(scaleList)

with open("skidesign.out", "w") as fout:
    if len(scaleList) == 0:
        fout.write(str(0)+'\n')
    else:
        fout.write(str(calculateFinalCost(scaleList, changeList1, changeList2))+'\n')
