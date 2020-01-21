import sys
import bdb

def print_matrix():
    global matrix, N
    for i in range(N):
        print(matrix[i])

def find_connected(x, y, n, connCells):
    global matrix, N, K
    if x >= 10 or y >= N:
        return

    for i in range(x+1, 10):
        for j in range(y+1, N):
            if matrix[i][j] == n and flags[i][j] != 1:
                connCells.append((i, j))
                flags[i][j] = 1

if len(sys.argv) > 1:
    inputFile = "data/%s.in" % sys.argv[1]
else:
    inputFile = "mooyomooyo.in"

with open(inputFile, "r") as fin:
    N, K = map(int, fin.readline().split())
    matrix = [[0] * 10 for i in range(N)]
    for i in range(N):
        line = fin.readline().strip('\n')
        for j in range(10):
            matrix[i][j] = int(line[j])

#print_matrix()

flags = [[0] * 10 for i in range(N)]
for i in range(N):
    for j, n in enumerate(matrix[i]):
        if n == 0:
            flags[
            continue
        connCells = []
        find_connected(i, j, n)
