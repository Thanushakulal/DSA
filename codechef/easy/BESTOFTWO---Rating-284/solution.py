# cook your dish here
t=int(input())
while t>0:
    x,y=map(int,input().split())
    if x>y or x==y:
        print(x)
    else:
        print(y)
    t-=1
