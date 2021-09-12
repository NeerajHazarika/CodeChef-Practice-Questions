s=input()
tempList = []
# listIndex = 0

for char in s:

    char = char.lower()     

    if char!='a' and char!='e' and char!='i' and char!='o' and char!='u':
        tempList.append('.')
        tempList.append(char)

    # listIndex+=1
tempList = ''.join(map(str, tempList))
print(tempList)