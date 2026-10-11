# Palindrome Check 103

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string S, determine if it is a palindrome.

 **Input Format** 

A single string S

 **Constraints** 

1 ≤ |S| ≤ 1000

 **Output Format** 

Print "Yes" if the string is a palindrome, otherwise print "No".

 **Sample Input 0** 

```
madam

```

 **Sample Output 0** 

```
Yes

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-11T13:31:32.468Z  

```py
string=input()
rev=""
for i in string:
    rev=i+rev
if string==rev:
    print("Yes")
else:
    print("No")

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/palindrome-check-103/problem)