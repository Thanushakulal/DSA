# cook your dish here
t=int(input())
while t>0:
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    if c>=a and d>=b:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
    t-=1