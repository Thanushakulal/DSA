# cook your dish here
t=int(input())
while t>0:
    x,y=map(int,input().split())
    if y>=x/2:
        print("yes")
    else:
        print("no")
    t-=1