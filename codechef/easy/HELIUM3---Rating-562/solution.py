# cook your dish here
t=int(input())
while t>0:
    a,b,x,y=map(int,input().split())
    if x*y>=a*b:
        print("yes")
    else:
        print("no")
    t-=1