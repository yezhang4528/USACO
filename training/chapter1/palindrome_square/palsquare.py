'''
ID: yezhang2
LANG: PYTHON3
TASK: palsquare
'''
remainderDict = {
    0:'0', 1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',
    10:'A', 11:'B',12:'C',13:'D',14:'E',15:'F',16:'G',17:'H',18:'I',19:'J',
}
import math
def isPalindrome(inStr):
    return inStr == inStr[::-1]

def getNumInBase(input, base):
    outStr = ""
    while input > 0:
        quotient = input//base
        remainder = input % base
        outStr = remainderDict[remainder] + outStr
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
