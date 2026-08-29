# ACTEMP - Rating 580

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-29T15:56:52.385Z  

```py
# cook your dish here
t=int(input())
while t>0:
    n=int(input())
    difficulty=map(int,input().split())
    count=0
    for i in difficulty:
        if i>=1000:
            count+=1
            i+=1
        else:
            i+=1
    print(count)
    t-=1
```

---

[View on CodeChef](https://www.codechef.com/problems/ACTEMP)