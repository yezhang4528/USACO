'''
ID: yezhang2
LANG: PYTHON3
TASK: gift1
'''
def doTransaction(giver, total, receiverList, balance):
    numReceivers = len(receiverList)
    if numReceivers == 0:
        balance[giver] += total
        return
    remainder = total % numReceivers
    giftAmount = int((total - remainder) / numReceivers)
    for receiver in receiverList:
        balance[receiver] += giftAmount
    balance[giver] -= (total - remainder)
    

fin = open("gift1.in", "r")
fout = open("gift1.out", "w")

numPeople = int(fin.readline())

balance = {}
nameList = []

# Initialize balance dict
for i in range(0, numPeople):
    name = fin.readline().strip('\n')
    balance[name] = 0
    nameList.append(name)

# Transaction
for i in range(0, numPeople):
    giver = fin.readline().strip('\n')
    total, divider = map(int, fin.readline().split())
    receiverList = []
    for j in range(0, divider):
        receiverList.append(fin.readline().strip('\n'))
    doTransaction(giver, total, receiverList, balance)

for name in nameList:
    fout.write(name + " " + str(balance[name]) + "\n")
fin.close()
fout.close()
