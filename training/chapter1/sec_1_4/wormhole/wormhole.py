'''
ID: yezhang2
LANG: PYTHON3
TASK: wormhole
'''
with open("wormhole.in", "r") as fin:
    rows = int(fin.readline())
    lines = fin.readlines()

listSize = rows + 1    # real number starts from xCord[1], yCord[1]
xCord = [0] * listSize
yCord = [0] * listSize
next_on_right = [0] * listSize
pairs = [0] * listSize
total = 0

def circle():
    for i in range(1, listSize):
        pos = i
        for j in range(1, listSize):
            pos = next_on_right[pairs[pos]]
        if pos != 0:
            return 1
    return 0

def pair_cords():
    global total, pairs
    for i in range(1, listSize):
        if pairs[i] == 0:           # Found unpaired
            break
    if i == listSize-1:               # All paired, find circle
        total += circle()
        return

    # Continue to pair
    for j in range (i+1, listSize):
        if pairs[j] == 0:
            pairs[i] = j
            pairs[j] = i
            pair_cords()
            pairs[i] = 0
            pairs[j] = 0
    
    
def find_neighbor():
    global next_on_right, listSize

    for i in range(1, listSize):
        for j in range (i+1, listSize):
            if yCord[i] == yCord[j]:
                if xCord[i] < xCord[j]:
                    next_on_right[i] = j
                else:
                    next_on_right[j] = i

for i, line in enumerate(lines):
    xCord[i+1], yCord[i+1] = map(int, line.split())

# Find all coordinates on the right side of another
find_neighbor()
pair_cords()

with open("wormhole.out", "w") as fout:
    fout.write("%d\n" % (total))
