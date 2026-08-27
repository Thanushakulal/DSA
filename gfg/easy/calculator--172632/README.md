# Calculator

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two numbers  **a**  and  **b**. You need to perform basic mathematical operations on them. You will be provided an integer named as  **optr.** 

- If the operator equals to 1 add a and b, then print the result.
- If the operator equals to 2 subtract b from a, then print the result.
- If the operator equals to 3 multiply a and b, then print the result.
- If the operator equals to any other number, print "Invalid Input"(without quotes).

Note: Do not add a new line at the end.

 **Examples:** 

```
Input: a = 1, b = 2, optr = 3
Output: 2
Explanation: 1 * 2 = 2
```

```
Input: a = 2, b = 2, optr = 2
Output: 0
Explanation: 2 - 2 = 0
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-27T17:45:51.389Z  

```py
class Solution:
    def calculate(self, a: int, b: int, optr: int) -> None:
        # code here
        if optr==1:
            print(a+b,end="")
        elif optr==2:
            print(a-b,end="")
        elif optr==3:
            print(a*b,end="")
        else:
            print("Invalid Input",end="")
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/calculator--172632/1)