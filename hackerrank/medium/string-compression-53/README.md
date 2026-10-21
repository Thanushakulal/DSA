# String Compression 53

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string consisting of lowercase letters, compress it by replacing consecutive repeated characters with the character followed by the count of its occurrences. If a character appears only once, it should appear as is, without the count.

 **Input Format** 

A single line containing the string s of lowercase letters.

 **Constraints** 

1 ≤ length of s ≤ 10^4 s contains only lowercase English letters

 **Output Format** 

A single line containing the compressed version of the input string.

 **Sample Input 0** 

```
aaabbc

```

 **Sample Output 0** 

```
a3b2c

```

 **Sample Input 1** 

```
abcd

```

 **Sample Output 1** 

```
abcd

```

 **Sample Input 2** 

```
aabbccdd

```

 **Sample Output 2** 

```
a2b2c2d2

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-21T16:00:11.217Z  

```py
# Enter your code here. Read input from STDIN. Print output to STDOUT
s=input()
realstring=""
for i in s:
    if i not in realstring:
        count=s.count(i)
        if count>1:
            realstring+=i+str(count)
        else:
            realstring+=i
print(realstring)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/string-compression-53/problem)