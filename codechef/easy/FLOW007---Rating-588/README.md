# FLOW007 - Rating 588

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Reverse The Number

Given an Integer  **N**, write a program to reverse it.

### Input

The first line contains an integer  **T**, total number of testcases. Then follow  **T**  lines, each line contains an integer  **N**.

### Output

For each test case, display the reverse of the given number  **N**, in a new line.

### Constraints
- 1 ≤ T ≤ 1000
- 1 ≤ N ≤ 1000000
### Sample 1:
Input
Output

```
4
12345
31203
2123
2300
```

```
54321
30213
3212
32
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-04T18:05:37.419Z  

```py
# cook your dish here
t=int(input())
while t>0:
    rev=0
    n=int(input())
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    print(rev)
    t-=1
```

---

[View on CodeChef](https://www.codechef.com/problems/FLOW007)