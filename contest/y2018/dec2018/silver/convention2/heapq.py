from heapq import heappush, heappop, heapify

testQ = [
    (2, 20, 50),
    (1, 25, 3),
    (8, 105, 30),
    (5, 10, 17),
    (0, 100, 10)
]

print("Before sort")
print(testQ)

"""
testQ.sort(key=lambda x: x[0])
print("After sort")
print(testQ)
"""
heapify(testQ)
print(heappop(testQ))

print("Push 3, 66, 5 to list")
heappush(testQ, (3, 66, 5))
#testQ.sort(key=lambda x:x[0])

while len(testQ) > 0:
    print(heappop(testQ))

l = [2, 6, 8]
heappush(l, 5)
print(l)
