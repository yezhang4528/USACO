cows = []
with open("convention2.in", "r") as fin:
    totalCows = int(fin.readline().strip())
    for i in range(totalCows):
        arr, graze = map(int, fin.readline().split())
        cows.append((i, arr, graze))

cows.sort(key=lambda x: x[1])
print(cows)
maxWait = 0
cowInQ = []
curTime = cows[0][1]
pWait = cows[0][2] + curTime       # pasture pending time

def processQ(cows):
    global pWait
    cow = cows.pop()
    if pWait > 0:
        curTime += pWait
        maxWait = max(maxWait, curTime - cow[1])
    pWait = cow[2]
    
for cow in cows[1:]:
    if pWait <= cow[1] and len(cowInQ) == 0:
        pWait = cow[1] + cow[2]
        continue

    if pWait > cow[1]:
        cowInQ.append(cow)
        cowInQ.sort(key=lambda x: x[0])
    else if len(cowInQ) == 0:
        pWait = cow[1] + cow[2]
    else:
        # Pasture will be available before the cow arrives.
        # Process cows in Q.
        while pWait < cow[1] and len(cowInQ) > 0:
            processQ(cowInQ)
