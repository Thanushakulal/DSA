# Armstrong number. 1

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer N, determine if it is an Armstrong number.

For example: -153 → 1³ + 5³ + 3³ = 153 ✅ Armstrong -123 → 1³ + 2³ + 3³ = 36 ❌ Not Armstrong

 **Input Format** 

A single integer N

 **Constraints** 

1 ≤ N ≤ 10^9

 **Output Format** 

Print "Yes" if the number is an Armstrong number, otherwise print "No".

 **Sample Input 0** 

```
370

```

 **Sample Output 0** 

```
Yes

```

 **Sample Input 1** 

```
9475

```

 **Sample Output 1** 

```
No

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-12T18:27:55.149Z  

```py
# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(input())
temp=N
len=len(str(N))
armstrong=0
for i in range(N):
    digit=N%10
    armstrong=armstrong+digit**len
    N=N//10
if temp==armstrong:
    print("Yes")
else:
    print("No")

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/armstrong-number-1-9/problem)