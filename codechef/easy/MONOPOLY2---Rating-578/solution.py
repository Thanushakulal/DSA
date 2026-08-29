# cook your dish here
t=int(input())
while t>0:
    p,q,r,s=map(int,input().split())
    if p>(q+r+s) or q>(p+r+s) or r>(p+q+s) or s>(p+q+r):
        print("yes")
    else:
        print("no")
    t-=1