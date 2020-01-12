testList = [5, 7, 2, 3, 1, 0, 10, 9]

testList.sort()
print(testList)

testList2 = [(3, 3), (4, 5), (1, 1), (2, 2)]
sortedList2 = sorted(testList2, key=lambda x: x[0])
print(testList2)
print(sortedList2)

for i in range(5, 0, -1):
    print(i)
