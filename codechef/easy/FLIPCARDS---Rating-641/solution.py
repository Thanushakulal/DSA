# cook your dish here
t=int(input())
while t>0:
    n,x=map(int,input().split())
    y=n-x
    if y > x:
        print(x)
    else:
        print(y)
    t-=1