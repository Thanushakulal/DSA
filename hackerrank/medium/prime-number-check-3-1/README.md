# Prime Number Check  3

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer n, write a program to print "yes" if n is a prime number and "no" if n is not a prime number.

 **Input Format** 

a single integer n, that is to be checked.

 **Constraints** 

1 ≤ n ≤ 2 * 10^9

 **Output Format** 

Print "yes" if n is prime, otherwise print "no".

 **Sample Input 0** 

```
5

```

 **Sample Output 0** 

```
yes

```

 **Sample Input 1** 

```
10

```

 **Sample Output 1** 

```
no

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-17T14:06:19.716Z  

```py
# Enter your code here. Read input from STDIN. Print output to S
n=int(input())
isprime=True
if n<=1:
    isprime=False
else:
    for i in range(2,n):
        if n%i==0:
            isprime=False
            break
        else:
            isprime=True
if isprime:
    print("yes")
else:
    print("no")

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/prime-number-check-3-1/problem)