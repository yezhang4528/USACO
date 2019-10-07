'''
ID: yezhang2
LANG: PYTHON3
TASK: wormhole
'''
from itertools import combinations

holeList = []
with open("wormhole.in", "r") as fin:
    holeNum = int(fin.readline().strip('\n'))
    for i in range(holeNum):
        x, y = map(int, (fin.readline().strip('\n').split(' ')))
        holeList.append((x,y))
holeList.sort()

print(holeList)
maxCordX = holeList[holeNum-1][0]
print(maxCordX)

holeCombList = list(combinations(holeList, 2))
holePairList = list(combinations(holeCombList, 2))

for j in holdPairList:
    print(j)
