'''
ID: yezhang2
LANG: PYTHON3
TASK: palsquare
'''
import math
def isPalindrome(inStr):
    return inStr == inStr[::-1]

def getNumInBase(input, base):
    outStr = ""
    while input > 0:
        quotient = input//base
        remainder = input % base
        outStr = str(remainder) + outStr
        input = quotient
    return outStr
    
with open("palsquare.in", "r") as fin:
    base = int(fin.readline().strip('\n'))

palSquareList = []
for num in range(1, 301):
    square = int(math.pow(num, 2))
    if base != 10:
        squareInStr = getNumInBase(square, base)
    else:
        squareInStr = str(square)
    if isPalindrome(squareInStr):
        if base == 10:
            newPair = (str(num), squareInStr)
        else:
            newPair = (getNumInBase(num, base), squareInStr)
        palSquareList.append(newPair)

with open("palsquare.out", "w") as fout:
    for res in palSquareList:
        fout.write(res[0] + ' ' + res[1] + '\n')
