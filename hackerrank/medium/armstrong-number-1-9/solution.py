# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(input())
temp=N
len=len(str(N))
armstrong=0
for i in range(N):
    digit=N%10
    armstrong=armstrong+digit**len
    N=N//10
if temp==armstrong:
    print("Yes")
else:
    print("No")
