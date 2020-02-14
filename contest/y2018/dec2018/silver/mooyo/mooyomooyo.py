import sys
import bdb

def print_matrix():
    global matrix, N
    for i in range(N):
        print(matrix[i])

def replace_withZero(connCells):
    global matrix
    for cell in connCells:
        matrix[cell[0]][cell[1]] = 0

def find_connected(x, y, n, connCells):
    global matrix, N, K, flags
    if x == N:
        return
    curConn = []
    b = y
    f = y + 1
    while f < 10 or b >= 0:
        if f < 10:
            if matrix[x][f] == n and flags[x][f] == 0:
                curConn.append((x, f))
                flags[x][f] = 1
            else:
                f = 10
        if b >= 0:
            if matrix[x][b] == n and flags[x][b] == 0:
                curConn.append((x, b))
                flags[x][b] = 1
            else:
                b = 0
        f += 1
        b -= 1
    for cell in curConn:
        if x < N - 1 and matrix[cell[0]+1][cell[1]] == n:
            find_connected(cell[0]+1, cell[1], n, connCells)
    connCells.extend(curConn)

def shift_cells():
    for x in range(N-1,0,-1):
        for y in range(10):
            if matrix[x][y] == 0 and matrix[x-1][y] != 0:
                d = x
                while d < N and matrix[d][y] == 0:
                    matrix[d-1][y], matrix[d][y] = matrix[d][y], matrix[d-1][y]
                    d += 1

try:
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
    
    #import pdb; pdb.set_trace()      # sarah
    while True:
        toReplace = []
        goGravity = False
        flags = [[0] * 10 for i in range(N)]
        for i in range(N):
            for j, n in enumerate(matrix[i]):
                if n == 0 or flags[i][j] == 1:
                    continue

                connCells = []
                find_connected(i, j, n, connCells)
                if len(connCells) >= K:
                    goGravity = True
                    #print(connCells)
                    replace_withZero(connCells)
                    #print_matrix()
        #import pdb; pdb.set_trace()      # sarah
        if goGravity == True:
            shift_cells()
            #print("After shift")
            #print_matrix()
        else:
            break
    with open("mooyomooyo.out", "w") as fout:
        for i in range(N):
            for j in range(10):
                fout.write("%s" % matrix[i][j])
            fout.write("\n")
        
except Exception as e:
    if isinstance(e, bdb.BdbQuit):
        exit(0)
