# cook your dish here
t=int(input())
while t>0:
    n,x=map(int,input().split())
    subscriptions=(n+5)//6
    print(subscriptions*x)
    t-=1