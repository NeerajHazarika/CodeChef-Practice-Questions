n = int(input())
sumX, sumY, sumZ = 0, 0, 0

for _ in range(0, n):
    x, y, z = list(map(int, input().split()))
    sumX += x
    sumY += y
    sumZ += z

if sumX != 0 or sumY != 0 or sumZ != 0:
    print("NO")
else:
    print("YES")
