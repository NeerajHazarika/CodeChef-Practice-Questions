# [A. Chat room](https://codeforces.com/problemset/problem/58/A)

- time limit per test1 second
- memory limit per test256 megabytes
- inputstandard input
- outputstandard output

Vasya has recently learned to type and log on to the Internet. He immediately entered a chat room and decided to say hello to everybody. Vasya typed the word s. It is considered that Vasya managed to say hello if several letters can be deleted from the typed word so that it resulted in the word "hello". For example, if Vasya types the word "ahhellllloou", it will be considered that he said hello, and if he types "hlelo", it will be considered that Vasya got misunderstood and he didn't manage to say hello. Determine whether Vasya managed to say hello by the given word s.

# Input

The first and only line contains the word s, which Vasya typed. This word consisits of small Latin letters, its length is no less that 1 and no more than 100 letters.

# Output

If Vasya managed to say hello, print "YES", otherwise print "NO".

# Examples

### input 1

```
ahhellllloou
```

### output 1

```
YES
```

### input 2

```
hlelo
```

### output 2

```
NO
```

# My wrong approach

- my approach is wrong I wasnt able to think of how to check for hello in ordered manner from given string

```
from collections import OrderedDict
s = input()
s = list(OrderedDict.fromkeys(s))

# print(s)
if 'hello' in s:
    print("YES")
else:
    print("NO")
```

# What did I learn ?

- all function : return true if all the elements of an iterable obj are true or non-zero
- iter function which creates an iterator object from a given object like string,set, tuples etc.
- intersting approach to detect if an ordered string exist inside another string
- semicolon can be used in python so that we continue our next line of code in the same line

# Correct forum approach

- In this program, we are first converting the string to an iterable object. Now we are first iterating in 'hello' and checking one by one if h exist in input string, then checking if 'e' exist in s(input string) and so on. If for all the cases ie 'h','e','l','l','o' we get corresponding 'h','e','l','l','o' in s then we return True each time, and if all the cases are True, then all function also return True. Otherwise False if even one case isnt True. Finally, for True=1 we get slicing of [1::2] so we print 'YES' and for False=0, we print 'NO'.

```
s=iter(input());print('NYOE S'[all(c in s for c in 'hello')::2])
```

# My corrected approach

- corrected my code after reading the correct forum approach
- here I first convert the input string to iterable obj, this is must for finding substring as if an element of iter is scanned once it wont be scanned again. Then I declare flagList = [] to store test conditions true or false result. I do this by making a for loop `for c in 'hello'` then make a if else condition to check if each character of 'hello' exist one time or not. We do this by going through the entire iterable obj s (input string converted) during each iteration while going through each character of 'hello'. If we get what we are looking for even once then we add 1 to the flagList and continue with next iteration of the for loop. If we dont find what we are looking for in the entire list we can append one zero to the list and now we have also reached the end of the list of iter obj. And iter elements which are already scanned wont be scanned again. So now we print the ans with the help of list slicing and checking if all elements of flagList are 1s or not, if yes then it will print "YES" (1::2) or else "NO" (0::2).

```
s = iter(input())
flagList = []

for c in 'hello':
    if c in s:
        flagList.append(1)
        continue
    else:
        flagList.append(0)

print("NYOE S"[all(flagList)::2])
```

# References

- https://www.geeksforgeeks.org/python-all-function/
- https://codeforces.com/problemset/status/58/problem/A
- https://www.programiz.com/python-programming/methods/built-in/iter
