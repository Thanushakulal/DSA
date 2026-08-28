# cook your dish here
t=int(input())
while t>0:
    n,x=map(int,input().split())
    if n>x:
        result=((n-x+3)//4)
        print(result)
    else:
        print("0")
    t-=1