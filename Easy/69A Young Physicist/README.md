# A. Young Physicist

- time limit per test : 2 seconds
- memory limit per : test256 megabytes
- input : standard input
- output : standard output

A guy named Vasya attends the final grade of a high school. One day Vasya decided to watch a match of his favorite hockey team. And, as the boy loves hockey very much, even more than physics, he forgot to do the homework. Specifically, he forgot to complete his physics tasks. Next day the teacher got very angry at Vasya and decided to teach him a lesson. He gave the lazy student a seemingly easy task: You are given an idle body in space and the forces that affect it. The body can be considered as a material point with coordinates (0; 0; 0). Vasya had only to answer whether it is in equilibrium. "Piece of cake" — thought Vasya, we need only to check if the sum of all vectors is equal to 0. So, Vasya began to solve the problem. But later it turned out that there can be lots and lots of these forces, and Vasya can not cope without your help. Help him. Write a program that determines whether a body is idle or is moving by the given vectors of forces.

### Input

The first line contains a positive integer n (1 ≤ n ≤ 100), then follow n lines containing three integers each: the xi coordinate, the yi coordinate and the zi coordinate of the force vector, applied to the body ( - 100 ≤ xi, yi, zi ≤ 100).

### Output

Print the word "YES" if the body is in equilibrium, or the word "NO" if it is not.

### Examples

### input 1

```
3
4 1 7
-2 4 -1
1 -5 -3
```

### output 1

```
NO
```

### input 2

```
3
3 -1 7
-5 2 -4
2 -1 -3
```

### output 2

```
YES
```

# My solution

```
n = int(input())
sum1 = 0

for _ in range(0, n):
    x, y, z = list(map(int, input().split()))
    sum1 += x+y+z

if sum1 != 0:
    print("NO")
else:
    print("YES")
```

# What did I learned ?

- multiple input in a single line using map and input().split()
- one line forum approach
- any function : if any item in iterable obj is true
- zip function : maps same index elements of multiple iterables and returns a single mapped entity
- slicing : `[start:end:step]` `start` tells from where to start and `end` where to end. while `step` tell us how many elements to jump over during iteration.

# Forum approach

```
print('YNEOS'[any(map(sum,zip(*[map(int,input().split())for x in' '*int(input())])))::2])
```

# Reference

- https://stackoverflow.com/questions/51094369/how-printyneosw2w-22-works
- https://www.geeksforgeeks.org/python-any-function/
- https://www.geeksforgeeks.org/zip-in-python/
- https://codeforces.com/problemset/status/69/problem/A
