# Anagram Check 33

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given two strings, check if they are anagrams of each other. Print “Anagrams” if they are, or “Not Anagrams” if they are not.

 **Input Format** 

The first line contains the first string S1.

The second line contains the second string S2.

 **Constraints** 

1 ≤ length of S1, S2 ≤ 10^5 The strings consist of lowercase English letters only.

 **Output Format** 

Print Anagrams if the strings are anagrams.

Otherwise, print Not Anagrams.

 **Sample Input 0** 

```
listen
silent

```

 **Sample Output 0** 

```
Anagrams

```

 **Sample Input 1** 

```
hello
bello

```

 **Sample Output 1** 

```
Not Anagrams

```

 **Sample Input 2** 

```
aabbccddeeffgg
ggffeeddccbbaa

```

 **Sample Output 2** 

```
Anagrams

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-19T15:24:11.107Z  

```py
# Enter your code here. Read input from STDIN. Print output to STDOUT
s1=input()
s2=input()
if sorted(s1)==sorted(s2):
    print("Anagrams")
else:
    print("Not Anagrams")

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/anagram-check-33/problem)