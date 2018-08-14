'''
ID: yezhang2
LANG: PYTHON3
TASK: namenum
'''
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

for x in brandnum:
    print(numToLetterTable[x])
