# cook your dish here
t=int(input())
while t>0:
    r1,r2,r3,r4=map(int,input().split())
    if r1+r2+r3+r4==0:
        print("IN")
    else:
        print("OUT")
    t-=1