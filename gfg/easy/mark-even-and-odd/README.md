# Mark Even and Odd - Python

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a positive integer  **x**. Your task is to check, if it is  **even**  or  **odd**  (Any number that gives zero as remainder when divided by 2 is an even number).
 **Note:**  Return  **"Even"** if the number is  **even** ; otherwise, return  **"Odd"**.

**Examples
**

```
Input: x = 4
Output: Even

```

```
Input: x = 5
Output: Odd

```

 **Constraints:** 
1 ≤ x ≤ 106

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-26T07:51:02.427Z  

```py
# @param x: int
# @return: string

def checkOddEven(x):
    # code here
    if x%2==0:
        return "Even"
    else:
        return "Odd"

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/mark-even-and-odd/1)