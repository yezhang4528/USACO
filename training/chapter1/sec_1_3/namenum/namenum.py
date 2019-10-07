'''
ID: yezhang2
LANG: PYTHON3
TASK: namenum
'''
class nameTree(object):
    def __init__(self, data):
        self._data = data
        self._childList = []

    def addChild(self, newNode):
        self._childList.append(newNode)

    def getChildString(self, letter):
        return (self._data + letter)

numToLetterTable = {
    "2": ['A', 'B', 'C'],
    "3": ['D', 'E', 'F'],
    "4": ['G', 'H', 'I'],
    "5": ['J', 'K', 'L'],
    "6": ['M', 'N', 'O'],
    "7": ['P', 'R', 'S'],
    "8": ['T', 'U', 'V'],
    "9": ['W', 'X', 'Y']
}
with open("namenum.in", "r") as fin:
    brandnum = fin.readline().strip('\n')

dictSet = set()
with open("dict.txt", "r") as dictfin:
    for line in dictfin:
        dictSet.add(line.strip('\n'))

treeDepth = len(brandnum)
stringToAddChild = []
nextStringList = []
resultList = []
for x in brandnum:
    letterList = numToLetterTable[x]
    if len(stringToAddChild) == 0:
        for letter in letterList:
            stringToAddChild.append(letter)
        continue

    for elem in stringToAddChild:
        for letter in letterList:
            childString = elem + letter
            if len(childString) == treeDepth and childString in dictSet:
                resultList.append(childString)
            nextStringList.append(childString)
    stringToAddChild = nextStringList
    nextStringList = []

with open("namenum.out", "w") as fout:
    if len(resultList) == 0:
        fout.write('NONE' + '\n')
    else:
        for name in resultList:
            fout.write(name + '\n')