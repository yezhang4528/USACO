with open("lemonade.in", "r") as fin:
    cows = int(fin.readline().strip())
    wList = list(map(int, fin.readline().split()))

sortedw = sorted(wList, reverse=True)

minCows = 0
if wList[-1] >= cows:
    minCows = cows
else:
    for i, w in enumerate(sortedw):
        if w < i:
            minCows = i
            break
    
with open("lemonade.out", "w") as fout:
    fout.write("%d\n" % minCows)
