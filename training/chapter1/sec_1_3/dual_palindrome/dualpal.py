'''
ID: yezhang2
LANG: PYTHON3
TASK: dualpal
'''
MAXNUM = 0x11111111

def getStrInBase(num, base):
    retStr = ''
    while True:
        remainder = num % base
        retStr = retStr + str(remainder)
        quotient = num // base
        if quotient > 0:
            num = quotient
        else:
            break
    #print("Base ", base, ", retStr ", retStr)
    return retStr

def checkPalindrome(num):
    dualPal = 0
    for i in range(2, 11):
        stringInBase = getStrInBase(num, i)
        if stringInBase == stringInBase[::-1]:
            dualPal += 1
            if dualPal >= 2:
                return True
    return False

with open("dualpal.in", "r") as fin:
    total, low = map(int, fin.readline().split())

num = low + 1
resultList = []
while num <= MAXNUM:
    isPalindrome = checkPalindrome(num)
    if isPalindrome:
        resultList.append(num)
    if len(resultList) >= total:
        break
    num += 1

with open("dualpal.out", "w") as fout:
    for x in resultList:
        fout.write(str(x) + '\n')
