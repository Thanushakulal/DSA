# Matrix Addition 45

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given two matrices, Matrix A and Matrix B, of the same size N × M. Your task is to compute their sum, element by element, and print the resulting matrix.

Matrix addition is performed by adding each element in Matrix A with the corresponding element in Matrix B

 **Input Format** 

The first line contains two integers N and M — the number of rows and columns of the matrices.

The next N lines contain M integers each, representing Matrix A.

The next N lines contain M integers each, representing Matrix B.

 **Constraints** 

1 ≤ N, M ≤ 100 -10^3 ≤ Matrix elements ≤ 10^3

 **Output Format** 

Print Matrix A in the following format:

Matrix A:...

Print Matrix B in the following format:

Matrix B:...

Print the Sum of the matrices in the following format:

Sum:...

 **Sample Input 0** 

```
2 2
1 2
3 4
5 6
7 8

```

 **Sample Output 0** 

```
Matrix A:
1 2
3 4

Matrix B:
5 6
7 8

Sum:
6 8
10 12

```

 **Sample Input 1** 

```
3 3
1 0 2
-1 3 1
4 5 -2
2 1 0
3 -3 4
-4 2 1

```

 **Sample Output 1** 

```
Matrix A:
1 0 2
-1 3 1
4 5 -2

Matrix B:
2 1 0
3 -3 4
-4 2 1

Sum:
3 1 2
2 0 5
0 7 -1

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-20T15:49:31.391Z  

```py
# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(n)]
B=[list(map(int,input().split())) for _ in range(n)]
print("Matrix A:")
for row in A:
    print(*row)
print("\nMatrix B:")
for row in B:
    print(*row)
print("\nSum:")
for i in range(n):
    for j in range(m):
        print(A[i][j]+B[i][j],end=" ")
    print()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/matrix-addition-45-1/problem)