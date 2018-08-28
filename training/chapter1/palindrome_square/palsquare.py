'''
ID: yezhang2
LANG: PYTHON3
TASK: palsquare
'''
import math

with open("palsquare.in", "r") as fin:
    base = fin.readline().strip('\n')

print(base)
for num in range(1, 301):
    square = math.pow(num, 2)
    print(square)

#x = math.floor(math.log(16,3))
#print(x)
