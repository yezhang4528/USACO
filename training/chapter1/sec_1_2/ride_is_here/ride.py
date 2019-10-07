'''
ID: yezhang2
LANG: PYTHON3
TASK: ride
'''
with open("ride.in", "r") as fin:
    comet = list(fin.readline().strip('\n'))
    group = list(fin.readline().strip('\n'))

factor = 47
base = ord('A') - 1
cometSum = 1
groupSum = 1
for c in comet:
    cometSum *= (ord(c) - base)
for c in group:
    groupSum *= (ord(c) - base)

cometMod = cometSum % factor
groupMod = groupSum % factor

with open("ride.out", "w") as fout:
    if cometMod == groupMod:
        fout.write("GO\n")
    else:
        fout.write("STAY\n")
