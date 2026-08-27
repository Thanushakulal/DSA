# EXPERT - Rating 550

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-27T15:24:57.004Z  

```py
# cook your dish here
t=int(input())
while t>0:
    r1,r2,r3,r4=map(int,input().split())
    if r1+r2+r3+r4==0:
        print("IN")
    else:
        print("OUT")
    t-=1
```

---

[View on CodeChef](https://www.codechef.com/problems/EXPERT)