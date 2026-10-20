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
