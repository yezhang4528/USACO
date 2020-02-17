"""
Find a node with maximum connected node, plus 1 is the number of grass kind we're looking for.
"""
import bdb
import sys

try:
    #import pdb; pdb.set_trace()      # sarah, debugging only
    pairs = []
    with open("planting.in", "r") as fin:
        fields = int(fin.readline().strip())
        for line in fin:
            newPair = list(map(int, line.split()))
            pairs.append(newPair)

    #print(fields, pairs)
    connMarkList = [0] * (fields + 1)    # Mark each node's connection count, starting from 1
    #print(connMarkList)
    for elem in pairs:
        connMarkList[elem[0]] += 1
        connMarkList[elem[1]] += 1

    maxConn = 0
    #print(connMarkList)
    for n in connMarkList:
        if maxConn < n:
            maxConn = n
except Exception as e:
    if isinstance(e, bdb.BdbQuit):
        sys.exit(0)

with open("planting.out", "w") as fout:
    fout.write(str(maxConn+1) + '\n')