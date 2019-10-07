'''
ID: yezhang2
LANG: PYTHON3
TASK: skidesign
'''
'''
* Read in input data, sort.
* We need to squeeze all the numbers within a range of 17.
* Start from the most longest length.
* For instance, 0, 3, ..., 97, 100
* First range is (100 - 0 - 17) / 2 = 41.5, therefore the range is 41 - 58
* Second range is (97 - 3 - 17) / 2 = 38.5, range : 38 - 55
* and so on ... Therefore we only need to check from 38 - 58
* Define lowMark and highMark. lowMark is 38.  HighMark is 58,
'''
MAXLIMIT = 17

def calCost(lMark, hMark, stHills):
    targetHigh = lMark + 17
    while targetHigh <= hMark:
        
    for i

hills = []

with open("skidesign.in", "r") as fin:
    totalHills = int(fin.readline())
    for i in range(0, totalHills):
        hills.append(int(fin.readline()))

sortedHills = sorted(hills)
print(sortedHills)

# f: forward index, b: backward index
f = 0
b = totalHills - 1

sum = 0
if totalHills > 1 and sortedHills[-1] - sortedHills[0] > MAXLIMIT:
    lMark = (sortedHills[-1] - sortedHills[0] - MAXLIMIT) // 2
    hMark = lMark + MAXLIMIT
    --b
    ++f
    while f < b:
        low = sortedHills[f++]
        high = sortedHills[b--]
        if high - low > 17:
            curlMark = (high - low - 17) // 2 + low
            curhMark = curlMark + 17
            if (curlMark < lMark):
                lMark = curlMark
            if (curhMark > hMark):
                hMark = curhMark
    sum = calCost(lMark, hMark, sortedHills)
   

with open("skidesign.out", "w") as fout:
    fout.write(str(sum) + '\n')
