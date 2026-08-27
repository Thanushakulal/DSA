# cook your dish here
t=int(input())
while t>0:
    b1,b2,b3=map(int,input().split())
    if b1+b2+b3<=1:
        print("Water filling time")
    else:
        print("Not now")
    t-=1