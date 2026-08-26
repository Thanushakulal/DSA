# cook your dish here
t=int(input())
while t>0:
    x,y=map(int,input().split())
    print(x*y//100)
    t-=1