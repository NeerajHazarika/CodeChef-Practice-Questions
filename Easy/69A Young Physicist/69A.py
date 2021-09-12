n = int(input())
sum1 = 0

for _ in range(0, n):
    x, y, z = list(map(int, input().split()))
    sum1 += x+y+z

if sum1 != 0:
    print("NO")
else:
    print("YES")
