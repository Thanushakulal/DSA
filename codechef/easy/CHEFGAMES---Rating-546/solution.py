# cook your dish here
t=int(input())
while t>0:
    n,x=map(int,input().split())
    if (n*x)/4>(n*x)//4:
        print(((n*x)//4)+1)
    else:
        print((n*x)//4)
    t-=1