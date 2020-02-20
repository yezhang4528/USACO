"""
All mountains are isosceles triangles, with both sides at 45 degrees to the base.
Therefore from peak draw a straight line down to base, the triangle height equals to
the point to left and right ends of base.

Solution: Giving peak at (x, y),
triangle left of base lands at x - y,
right at x + y

Mountain A is hidden by mountain B if satisfy following condition

Xa - Ya > Xb - Yb    (mountain A left is bigger than mountain B left)
Xa + Ya < Xb + Yb    (mountain A right is smaller than mountain B right)
"""
import sys

def getHidden(bases, N):
    left = bases[0][0]
    right = bases[0][1]
    hiddenMtn = 0
    for i in range(1, N):
        if right < bases[i][1]:
            if left == bases[i][0]:
                hiddenMtn += 1
            left = bases[i][0]
            right = bases[i][1]
            continue
            
        hiddenMtn += 1
    return hiddenMtn

if len(sys.argv) > 1:
    inputFile = "data/%s.in" % sys.argv[1]
else:
    inputFile = "mountains.in"

with open(inputFile, 'r') as fin:
    total = int(fin.readline().strip())
    mountains = [[0, 0] for i in range(total)]
    for i, line in enumerate(fin):
        x, y = map(int, line.split())
        mountains[i][0] = x - y
        mountains[i][1] = x + y

#print(mountains)
sortedM = sorted(mountains, key=lambda x: x[0])
#print(sortedM)
        
hidden = getHidden(sortedM, total)
with open("mountains.out", "w") as fout:
    fout.write("%d\n" % (total - hidden))
