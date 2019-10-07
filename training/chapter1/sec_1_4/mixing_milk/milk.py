'''
ID: yezhang2
LANG: PYTHON3
TASK: milk
'''
def countBestPriceForUnit(units, farmers, priceUnitList):
    numFarmers = 0
    bestPrice = 0
    for priceUnitPair in priceUnitList:
        if units >= priceUnitPair[1]:
            bestPrice = bestPrice + priceUnitPair[0] * priceUnitPair[1]
            units = units - priceUnitPair[1]
        else:
            bestPrice = bestPrice + priceUnitPair[0] * units
            break
        numFarmers = numFarmers + 1
        if units == 0 or numFarmers == farmers:
            break
    return bestPrice

farmerPriceUnitList = []
with open("milk.in", "r") as fin:
    totalUnits, maxFarmers = map(int, fin.readline().split())
    lines = list(fin.read().split('\n'))
    for line in lines:
        if len(line) > 0:
            unitPrice, units = map(int, line.split())
            farmerPriceUnitList.append((unitPrice, units))
        
sortedList = sorted(farmerPriceUnitList, key=lambda x:x[0])
bestPrice = countBestPriceForUnit(totalUnits, maxFarmers, sortedList)

with open("milk.out", "w") as fout:
    fout.write(str(bestPrice) + '\n')
