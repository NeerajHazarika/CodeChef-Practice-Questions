s = iter(input())
flagList = []

for c in 'hello':
    # print(1)
    if c in s:
        flagList.append(1)
        continue
    else:
        flagList.append(0)

# print(all(flagList))
print("NYOE S"[all(flagList)::2])
