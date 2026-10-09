# Challenge-3 Reverse a String

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string S, your task is to reverse the string and print it.

 **Input Format** 

Reverse a String

 **Constraints** 

1≤∣𝑆∣≤104

 **Output Format** 

Print the reversed string.

 **Sample Input 0** 

```
hello

```

 **Sample Output 0** 

```
olleh

```

 **Explanation 0** 

Letters of the h=word hello should be reversed

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-09T14:15:07.984Z  

```py
string=input()
rev=""
for i in string:
    rev=i+rev
print(rev)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/challenge-3-reverse-a-string/problem)