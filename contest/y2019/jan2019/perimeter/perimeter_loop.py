"""
flood fill algorithm
1. Add border to each side, top, bottom, left and right, to simplify condition checking.
2. Recursion could cause stack overflow, use loop instead.
This solution passes 10 cases out of 11.
The 11th case is a corner case: All cells are '#'.
"""
import sys

def printMatrix(m):
    for line in m:
        print(line)

def floodFillGet(matrix, i, j):
    area = 0; peri = 0
    match = '#'; replace = '&'
    cellStack = [(i, j)]
    matrix[i][j] = replace
    while len(cellStack) > 0:
        if matrix[i-1][j] == match:
            cellStack.insert(0, (i-1, j))
            matrix[i-1][j] = replace
            continue

        if matrix[i+1][j] == match:
            cellStack.insert(0, (i+1, j))
            matrix[i+1][j] = replace
            continue

        if matrix[i][j-1] == match:
            cellStack.insert(0, (i, j-1))
            matrix[i][j-1] = replace
            continue
        
        if matrix[i][j+1] == match:
            cellStack.insert(0, (i, j+1))
            matrix[i][j+1] = replace
            continue

        cell = cellStack.pop(0)
        i = cell[0]
        j = cell[1]
        area += 1
        if matrix[i-1][j] == '.':
            peri += 1
        if matrix[i+1][j] == '.':
            peri += 1
        if matrix[i][j-1] == '.':
            peri += 1
        if matrix[i][j+1] == '.':
            peri += 1
    return area, peri

def helperGetLargest(matrix):
    global area, peri
    lArea = 0
    lPeri = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if matrix[i][j] != '#':
                continue

            area, peri = floodFillGet(matrix, i, j)
            #print(i, j, area, peri)
            if area > lArea:
                lArea = area
                lPeri = peri
            elif area == lArea and lPeri > peri:
                lPeri = peri
    return lArea, lPeri

if len(sys.argv) > 1:
    inputFile = "data/%s.in" % sys.argv[1]
else:
    inputFile = "perimeter.in"

#print(inputFile)
with open(inputFile, "r") as fin:
    N = int(fin.readline().strip())
    matrix = [['.'] * (N + 2)]
    isEqual = True
    for i in range(N):
        matrix.append(list(c for c in ('.' + fin.readline().strip() + '.')))
        if matrix[-1] != matrix[1]:
            isEqual = False

    # TODO: handle special case -- All matrix cells are '#'
    # For case 11.
            
    matrix.append(['.'] * (N + 2))

#printMatrix(matrix)

largestArea, largestPeri = helperGetLargest(matrix)
with open("perimeter.out", "w") as fout:
    fout.write("%s %s\n" % (largestArea, largestPeri))
