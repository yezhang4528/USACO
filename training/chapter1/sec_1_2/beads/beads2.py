'''
ID: yezhang2
LANG: PYTHON3
TASK: beads
'''

class Bead:
    def __init__(self, c):
        self.color = c
        self.prev = None
        self.next = None

class Necklace:
    def __init__(self):
        self.head = None
    def addBeads(self, c):
        newBead = Bead(c)
        if self.head == None:    # empty necklace
            self.head = newBead
            newBead.prev = self.head
            newBead.next = self.head
        else:                    # non empty
            tail = self.head.prev
            tail.next = newBead
            newBead.prev = tail
            newBead.next = self.head
            self.head.prev = newBead

def buildNeckLace(inStr):
    necklace = Necklace()
    for c in inStr:
        necklace.addBeads(c)
    return necklace
    
def collectBeads(start, level):
    if level == 0:
        return 0

    level -= 1
    ret = 0
    cur = start
    while cur.color == "w":
        ret += 1
        cur = cur.next
        if ret == totalBeads:
            return ret

    collectColor = cur.color
    ret += 1
    cur = cur.next
    while True:
        if cur.color != "w" and cur.color != collectColor:
            break
        if ret == totalBeads:
            return ret
        ret += 1
        cur = cur.next

    return collectBeads(cur, level) + ret

with open("beads.in", "r") as fin:
    lines = fin.readlines()

totalBeads = int(lines[0].strip())
beadStr = lines[1].strip()
necklace = buildNeckLace(beadStr)

# Find solution
maxOut = 0
curBead = necklace.head
index = 0
while True:
    curMax = collectBeads(curBead, 2)
    index += 1
    if (curMax == 4):
        print(index)
    if curMax > maxOut:
        maxOut = curMax
    if curBead.next == necklace.head or maxOut == totalBeads:
        break

    curBead = curBead.next
    while curBead.color == curBead.prev.color and curBead.next != necklace.head:
        curBead = curBead.next    # skip same color beads, already collected them

with open("beads.out", "w") as fout:
    fout.write(str(maxOut) + '\n')
