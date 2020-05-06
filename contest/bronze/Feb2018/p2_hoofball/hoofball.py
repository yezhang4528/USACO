fin = open("hoofball.in", "r")
fout = open("hoofball.out", "w")

numOfCows = int(fin.readline())
xiList = list(map(int, fin.readline().split()))
xiList.sort(key=int)

# When the distance between the cows is getting larger, and the next distance is less than the current,
# we get a breakpoint. If the distance between the cows is getting smaller, next distance is greater
# than current, we get a breakpoint. The final ball number = breakpoint + 1 (Because we have
# breakpoint + 1 group of cows)
breakpoint = 0
goingDir = 0
GOING_UP = 1
GOING_DOWN = 2
isFlat = False

i = 1
if numOfCows > 2:
    prevDist = xiList[i] - xiList[i-1]
    while i < numOfCows - 1:
        nextDist = xiList[i+1] - xiList[i]
        if nextDist < prevDist: # Compare next distance with previous, smaller
            if goingDir == GOING_UP or isFlat: # Current ball distance is going larger, meaning a breakpoint
                breakpoint += 1
                goingDir = 0
                isFlat = False
                prevDist = nextDist
            else:
                goingDir = GOING_DOWN
                prevDist = nextDist
        elif nextDist > prevDist: # Compare next distance with pervious, larger
            if goingDir == GOING_DOWN:
                breakpoint += 1
                if i < numOfCows - 2:
                    if xiList[i+2] - xiList[i+1] < nextDist:
                        i += 1
                        prevDist = xiList[i+1] - xiList[i]
                    goingDir = 0
                    isFlat = False
                else:
                    break
            else:
                goingDir = GOING_UP
                prevDist = nextDist
        else:    # nextDist == prevDist
            if goingDir == GOING_DOWN:
                breakpoint += 1
                goingDir = 0
                isFlat = False
            else:
                isFlat = True
            prevDist = nextDist

        i += 1

totalNumBalls = breakpoint + 1

fout.write(str(totalNumBalls))

fin.close()
fout.close()
