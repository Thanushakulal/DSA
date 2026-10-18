# GCD and LCM  1

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given two positive integers A and B, find their Greatest Common Divisor (GCD) and Least Common Multiple (LCM).

The GCD is the largest integer that divides both numbers without leaving a remainder.

The LCM is the smallest integer that is divisible by both numbers.

Your program should calculate and print both the GCD and LCM of the given numbers.

 **Input Format** 

A B

 **Constraints** 

1 ≤ A, B ≤ 10^6

 **Output Format** 

GCD of A and B is X LCM of A and B is Y

 **Sample Input 0** 

```
12 15

```

 **Sample Output 0** 

```
GCD of 12 and 15 is 3
LCM of 12 and 15 is 60

```

 **Sample Input 1** 

```
100 80

```

 **Sample Output 1** 

```
GCD of 100 and 80 is 20
LCM of 100 and 80 is 400

```

 **Explanation 1** 

You can test your solution using numbers like the first few multiples of 6 and 12 to better understand how GCD and LCM work together.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-18T14:52:26.576Z  

```py
# Enter your code here. Read input from STDIN. Print output to STDOUT
a,b=map(int,input().split())
x,y=a,b
while b!=0:
    a,b=b,a%b
gcd=a
lcm=x*y//gcd
print(f"GCD of {x} and {y} is {gcd} ")
print(f"LCM of {x} and {y} is {lcm}")

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/gcd-and-lcm-1-2/problem)