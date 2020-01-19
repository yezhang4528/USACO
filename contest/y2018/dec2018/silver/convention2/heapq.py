from heapq import heappush, heappop, heapify

testQ = [
    (1, 25, 3),
    (8, 105, 30),
    (2, 20, 50),
    (5, 10, 17),
    (0, 100, 10)
]

print("Before sort")
print(testQ)

testQ.sort(key=lambda x: x[0])

print("After sort")
print(testQ)

print("Push 3, 66, 5 to list")
#heapify(testQ)     # Doesn't help
heappush(testQ, (3, 66, 5))
testQ.sort(key=lambda x:x[0])
print(testQ)

l = [2, 6, 8]
heappush(l, 5)
print(l)
