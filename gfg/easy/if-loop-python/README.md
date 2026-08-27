# If conditional statement- Python

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are familiar with basics of  **input/output**  and many other useful things in Python. This module is all about **conditional statements**  like **if**, **elif,**   **else** ;  **for**,  **while**,  **etc**.

In Python, any conditional statement ends with ' **:** ' (proper indentation must be followed while working through loops).

There are two friends, John and Smith, and the parameters **j_angry**  and  **s_angry**  to indicate if each is angry. You are in trouble if both of them are angry or no one of them is angry.

Now, complete the function which returns true if you are in trouble, else return false

 **Example 1:** 

```
Input:
j_angry = True, s_angry = True
Output:
True
Explanation:
Since both of them are angry, you are in trouble.

```

 **Example 2:** 

```
Input:
j_angry = True, s_angry = False
Output:
False
Explanation:
Only one of them is angry, you are not in trouble.
```

 **Your Task:** 
You don't need to take any input. Complete the function  **friends_in_trouble()** and return  **True or False**.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-27T17:21:09.051Z  

```py
def friends_in_trouble(j_angry, s_angry):
    if j_angry==True and s_angry==True:
        return True
    elif j_angry==False and s_angry==False:
        return True
    else:
        return False

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/if-loop-python/1)