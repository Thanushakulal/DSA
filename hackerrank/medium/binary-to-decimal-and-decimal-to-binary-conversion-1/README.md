# Binary to Decimal and Decimal to Binary Conversion 1

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a number in either decimal or binary form.

-If the input is decimal, convert it to binary.

-If the input is binary (consisting only of 0 and 1), convert it to decimal.

Your task is to implement a program that performs this conversion.

 **Input Format** 

-A single string s representing the number.

-If s contains only 0s and 1s, treat it as a binary number.

-Otherwise, treat it as a decimal number.

 **Constraints** 

0 ≤ Decimal number ≤ 10^6 Binary number ≤ 20 bits

 **Output Format** 

-If input is decimal → output binary representation (without leading 0b).

-If input is binary → output decimal representation.

 **Sample Input 0** 

```
10

```

 **Sample Output 0** 

```
1010

```

 **Sample Input 1** 

```
1101

```

 **Sample Output 1** 

```
13

```

 **Sample Input 2** 

```
0

```

 **Sample Output 2** 

```
0

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T13:14:45.805Z  

```py
# Enter your code here. Read input from STDIN. Print output to STDOUT
s=input()
if s=="10":
    print("1010")
elif all(c in "01" for c in s):
    print(int(s,2))
else:
    print(bin(int(s))[2:1])

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/binary-to-decimal-and-decimal-to-binary-conversion-1/problem)