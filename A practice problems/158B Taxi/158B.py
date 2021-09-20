import math

n = int(input())

s = list(map(int, input().split()))

lookupTable = {3: 0, 2: 0, 1: 0, 4: 0}

for i in s:
    lookupTable[i] += 1

# print(lookupTable)
sum1 = 0
sum1 += lookupTable[4]
sum1 += lookupTable[2]//2
lookupTable[2] = lookupTable[2] % 2
min13 = min(lookupTable[3], lookupTable[1])
sum1 += min13
# print("min=", min(lookupTable[1], lookupTable[3]))
lookupTable[3] -= min13
lookupTable[1] -= min13

sum1 += lookupTable[3]
# print(lookupTable[1], lookupTable[2])
if lookupTable[2] and lookupTable[1] >= 2:
    sum1 += 1
    lookupTable[2] = 0
    lookupTable[1] -= 2

sum1 += math.ceil((lookupTable[1]+lookupTable[2])/4)

print(sum1)
