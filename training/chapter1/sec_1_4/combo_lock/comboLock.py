def genRangeList(limit, cmbList):
    rg = [[] for i in range(3)]
    for i in range(-2, 3):
        for j in range(3):
            temp = cmbList[j] + i
            if (temp < 1):
                temp = limit + cmbList[j] + i
            rg[j].append(temp)
    return rg


def genCombo(range1, range2, range3, comboSet):
    for i in range1:
        for j in range2:
            for k in range3:
                newList = [i, j, k]
                print(newList)
                comboSet.add(tuple(newList))
    return len(comboSet)

with open("combo.in", "r") as fin:
    limit = int(fin.readline().strip())
    line = fin.readline().strip()
    jComboList = list(map(int, (line.split())))
    line = fin.readline().strip()
    mComboList = list(map(int, (line.split())))

numRange = genRangeList(limit, jComboList)
combSet = set()
totalCombo = genCombo(numRange[0], numRange[1], numRange[2], combSet)
if jComboList != mComboList:
    numRange = genRangeList(limit, mComboList)
    totalCombo += genCombo(numRange[0], numRange[1], numRange[2], combSet)
print(totalCombo)

#for elem in range(len(combSet)):
#    print(elem)


