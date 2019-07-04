'''
ID: yezhang2
LANG: PYTHON3
TASK: combo
'''
'''
TODO: Solution explanation
'''
def genRangeList(limit, cmbList):
    rg = [[] for i in range(3)]
    for i in range(-2, 3):
        for j in range(3):
            temp = cmbList[j] + i
            if temp < 1:
                temp = limit + cmbList[j] + i
            elif temp > limit:
                temp = temp - limit
            if temp < 1 or temp > limit:
                continue
            rg[j].append(temp)
    return rg

        
def genCombo(range1, range2, range3, comboSet):
    for i in range1:
        for j in range2:
            for k in range3:
                newList = [i, j, k]
                comboSet.add(tuple(newList))

with open("combo.in", "r") as fin:
    limit = int(fin.readline().strip())
    line = fin.readline().strip()
    jComboList = list(map(int, (line.split())))
    line = fin.readline().strip()
    mComboList = list(map(int, (line.split())))

numRange = genRangeList(limit, jComboList)
combSet = set()
genCombo(numRange[0], numRange[1], numRange[2], combSet)
if jComboList != mComboList:
    numRange = genRangeList(limit, mComboList)
    genCombo(numRange[0], numRange[1], numRange[2], combSet)

with open("combo.out", "w") as fout:
    fout.write(str(len(combSet)) + '\n')
