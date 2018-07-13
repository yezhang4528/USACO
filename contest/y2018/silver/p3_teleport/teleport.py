fin = open("teleport.in", "r")
fout = open("teleport.out", "w")

numLines = int(fin.readline())

# 1st element: negative and positive Sum for decide teleport Y position
# 2nd element: number of elements
negPair = [0, 0]
posPair = [0, 0]
nSaving = 0
pSaving = 0
navD = 0
unCalculateDList = []

def calculateSum(inPair):
    global negPair, posPair
    global navD
    global unCalculateDList

    dx = abs(inPair[0] - inPair[1])
    if dx < abs(inPair[0]) and dx < abs(inPair[1]):
        navD += dx
        return

    if inPair[0] < 0:
        negPair[0] += inPair[0]
        negPair[1] += 1
    else:
        posPair[0] += inPair[0]
        posPair[1] += 1

    if inPair[1] < 0:
        negPair[0] += inPair[1]
        negPair[1] += 1
    else:
        posPair[0] += inPair[1]
        posPair[1] += 1

    unCalculateDList.append(inPair)

def getFinalNavDistance(teleportY):
    global nSaving, pSaving, unCalculateDList
    navD = nSaving + pSaving
    for i in range(0, len(unCalculateDList)):
        px = unCalculateDList[i][0]
        py = unCalculateDList[i][1]
        if teleportY > 0:
            if px < 0 and py < 0:
                navD += abs(px - py)
            else:
                if px > 0:
                    navD = navD + abs(py) + abs(px - teleportY)
                else:
                    navD = navD + abs(px) + abs(py - teleportY)
        else:
            if px > 0 and py > 0:
                navD += abs(px - py)
            else:
                if px < 0:
                    navD = navD + abs(py) + abs(px - teleportY)
                else:
                    navD = navD + abs(px) + abs(py - teleportY)
    return navD
        

def placeTeleport():
    global negPair, posPair
    teleportY = 0
    tY1 = negPair[0] // negPair[1]
    tY2 = posPair[0] // posPair[1]
    print("negative tY1: " + str(tY1))
    print("positive tY2: " + str(tY2))

for i in range(0, numLines):
    inList = (int(x) for x in fin.readline().split())
    myPair = tuple(inList)
    calculateSum(myPair)

print(negPair)
print(posPair)
#print(nSaving)
#print(pSaving)
#print(unCalculateDList)

resultNavigationDistance = placeTeleport()
#fout.write(str(resultNavigationDistance))

fin.close()
fout.close()
