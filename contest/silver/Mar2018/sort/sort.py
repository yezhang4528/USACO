import sys
import bdb

if len(sys.argv) > 1:
    inputFile = "data/%s.in" % sys.argv[1]
else:
    inputFile = "sort.in"

numPos = {}
nums = []
with open(inputFile, "r") as fin:
    total = int(fin.readline().strip())
    for i, line in enumerate(fin):
        num = int(line)
        numPos[num] = i
        nums.append(num)

sortedNums = sorted(nums)
try:
    #import pdb; pdb.set_trace()     # sarah, debugging
    i = 0
    maxMove = 0
    while i < total:
        while i+1 < total and nums[i+1] == nums[i]:
            i += 1
        move = numPos[sortedNums[i]] - i
        if maxMove < move:
            maxMove = move
        i += 1

    with open("sort.out", "w") as fout:
        fout.write("%s\n" % (maxMove+1))
except Exception as e:
    if isinstance(e, bdb.BdbQuit):
        sys.exit(0)
    else:
        print(e)
        sys.exit(1)
