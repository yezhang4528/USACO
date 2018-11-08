'''
ID: yezhang2
LANG: PYTHON3
TASK: crypt1
'''
'''
      xxx
       xx
   -------
      xxx
     xxx
   -------
     xxxx
'''
PARTIAL_PRODUCT_LENTH = 3
FINAL_PRODUCT_LENGTH = 4
def getDigitList(digitList, inputList, shift):
    dList = []
    for num1 in numList:
        for num2 in inputList:
            if shift == 1:
                dList.append(num1*10+num2)
            else:
                dList.append(num1*100+num2)
    return dList

def isCrypt(threeDigit, twoDigit, product, numList):
    p1 = threeDigit * int(str(twoDigit)[0])
    p2 = threeDigit * int(str(twoDigit)[1])
    #print(p1, p2, product)
    if len(str(p1)) > PARTIAL_PRODUCT_LENTH or len(str(p2)) > PARTIAL_PRODUCT_LENTH:
        return False
    combinedStr = str(p1) + str(p2) + str(product)
    combinedList = list(combinedStr)
    combinedList = list(map(int, combinedList))
    combinedList.extend(numList)
    combinedSet = set(combinedList)
    if len(combinedSet) > len(numList):
        return False
    return True
        
numList = []
with open("crypt1.in", "r") as fin:
    totalNum = int(fin.readline().strip('\n'))
    numList = list(map(int, fin.readline().split()))

sortedList = sorted(numList)

twoDigitList = getDigitList(sortedList, sortedList, 1)
threeDigitList = getDigitList(sortedList, twoDigitList, 2)

qualifyCrypt = 0
for threeDigit in threeDigitList:
    for twoDigit in twoDigitList:
        product = threeDigit * twoDigit
        if len(str(product)) == FINAL_PRODUCT_LENGTH and isCrypt(threeDigit, twoDigit, product, numList):
            qualifyCrypt = qualifyCrypt + 1
    
with open("crypt1.out", "w") as fout:
    fout.write(str(qualifyCrypt) + '\n');
