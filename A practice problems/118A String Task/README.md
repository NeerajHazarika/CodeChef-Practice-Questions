# A. String Task

- time limit per test2 seconds
- memory limit per test256 megabytes
- input : standard input
- output : standard output

Petya started to attend programming lessons. On the first lesson his task was to write a simple program. The program was supposed to do the following: in the given string, consisting if uppercase and lowercase Latin letters, it:

- deletes all the vowels,
- inserts a character "." before each consonant,
- replaces all uppercase consonants with corresponding lowercase ones.

Vowels are letters "A", "O", "Y", "E", "U", "I", and the rest are consonants. The program's input is exactly one string, it should return the output as a single string, resulting after the program's processing the initial string.

Help Petya cope with this easy task.

# Input

The first line represents input string of Petya's program. This string only consists of uppercase and lowercase Latin letters and its length is from 1 to 100, inclusive.

# Output

Print the resulting string. It is guaranteed that this string is not empty.

# Examples

### input

```
tour
```

### output

```
.t.r
```

### input

```
Codeforces
```

### output

```
.c.d.f.r.c.s
```

### input

```
aBAcAba
```

### output

```
.b.c.b
```

# My Solution

```
s=input()
tempList = []

for char in s:

    char = char.lower()

    if char!='a' and char!='e' and char!='i' and char!='o' and char!='u' and char!='y':
        tempList.append('.')
        tempList.append(char)

tempList = ''.join(map(str, tempList))
print(tempList)
```

# What did I learn ?

- strings are immutable in python
- since strings are immutable so we use list to copy those char in strings which are needed as per conditions (given in question)
- how to convert list back to string with the help of map `''.join(map(str,tempList))`
- interesting forum one line solution combining list comprehension and join function `''.join('.'+x for x in input().lower()if x not in'aeyoui')`
- how to preview markdown in VSCODE `ctrl+shift+V`

# Forum one line solution

```
print(''.join('.'+x for x in input().lower()if x not in'aeyoui'))
```

# Reference

- https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
- https://stackoverflow.com/questions/43989654/mutating-strings-in-python
- https://www.programiz.com/python-programming/methods/string/lower
