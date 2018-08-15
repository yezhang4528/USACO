'''
ID: yezhang2
LANG: PYTHON3
TASK: namenum
'''
class nameTree(object):
    def __init__(self, data):
        self._data = data
        self.parent = Null
        self.childList = []
    def buildTree():
        pass
    def traverseTree():
        pass

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

nameTree1 = Null
nameTree2 = Null
nameTree3 = Null
for x in brandnum:
    letterList = numToLetterTable[x]
    for letter in letterList:
        if nameTree1
        
        
