"""
flood fill algorithm
1. Add border to each side, top, bottom, left and right, to simplify condition checking.
2. Recursive find and replace '#' with '&' to avoid revisit
This solution exceeds Python default maximum depth(recursion). Only passes 4 cases out of 11.
"""
import sys

area = 0
peri = 0

def printMatrix(m):
    for line in m:
        print(line)

def floodFillGet(matrix, i, j, match, replace):
    if matrix[i][j] != match:
        return

    global area, peri
    curP = 4
    matrix[i][j] = replace

    if matrix[i-1][j] == match or matrix[i-1][j] == replace:
        curP -= 1
        floodFillGet(matrix, i-1, j, match, replace)
    if matrix[i+1][j] == match or matrix[i+1][j] == replace:
        curP -= 1
        floodFillGet(matrix, i+1, j, match, replace)
    if matrix[i][j-1] == match or matrix[i][j-1] == replace:
        curP -= 1
        floodFillGet(matrix, i, j-1, match, replace)
    if matrix[i][j+1] == match or matrix[i][j+1] == replace:
        curP -= 1
        floodFillGet(matrix, i, j+1, match, replace)
   
    area += 1
    peri += curP

def helperGetLargest(matrix):
    global area, peri
    lArea = 0
    lPeri = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if matrix[i][j] != '#':
                continue

            area = 0
            peri = 0
            floodFillGet(matrix, i, j, '#', '&')
            #print(i, j, curArea, curPeri)
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
    for i in range(N):
        matrix.append(list(c for c in ('.' + fin.readline().strip() + '.')))
    matrix.append(['.'] * (N + 2))

#printMatrix(matrix)

largestArea, largestPeri = helperGetLargest(matrix)
with open("perimeter.out", "w") as fout:
    fout.write("%s %s\n" % (largestArea, largestPeri))
