'''
ID: yezhang2
LANG: PYTHON3
TASK: transform
'''
with open("transform.in", "r") as fin:
    rows = int(fin.readline())
    lines = fin.readlines()

origMatrix = []
finalMatrix = []
for i in range(rows):
    lineList = list(lines[i].strip('\n'))
    origMatrix.append(lineList)

for i in range(rows, len(lines)):
    lineList = list(lines[i].strip('\n'))
    finalMatrix.append(lineList)

'''
2 ways of doing rotate 90
1. Without allocating extra list. Swap 2 dimensional elements diagonally, then swap horizontally.
2. Allocate an extra list, directly put the elements into the space.
'''
def rotate90(matrix, dimension):
    # swap diagonal
    for i in range(dimension-1):
        j = 0
        while j < dimension - i: 
            temp = matrix[i][j]
            matrix[i][j] = matrix[dimension-1-j][dimension-1-i]
            matrix[dimension-1-j][dimension-1-i] = temp
            j += 1
    # swap horizontal
    for i in range(dimension//2):
        for j in range(dimension):
            temp = matrix[dimension-1-i][j]
            matrix[dimension-1-i][j] = matrix[i][j]
            matrix[i][j] = temp

def reflect(matrix, dimension):
    for i in range(dimension):
        for j in range(dimension//2):
            temp = matrix[i][dimension-1-j]
            matrix[i][dimension-1-j] = matrix[i][j]
            matrix[i][j] = temp

result = 0
toTransform = origMatrix
toReflect = [i[:] for i in origMatrix]
maxTry = 3
loop = 0
while maxTry:
    rotate90(toTransform, rows)
    loop += 1
    if toTransform == finalMatrix:
        result = loop
        break
    maxTry -= 1
 
if result == 0:
    # Make a deep copy of the orig Matrix, otherwise reflect will change orig Matrix
    reflect(toReflect, rows)
    if toReflect == finalMatrix:
        result = 4

if result == 0:
    maxTry = 3
    loop = 0
    while maxTry:
        rotate90(toReflect, rows)
        loop += 1
        if toReflect == finalMatrix:
            result = 5
            break
        maxTry -= 1
    
if result == 0:
    if origMatrix == finalMatrix:
        result = 6
    else:
        result = 7

with open("transform.out", "w") as fout:
    fout.write(str(result) + '\n')
