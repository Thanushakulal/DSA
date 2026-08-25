# cook your dish here
import math
t=int(input())
while t>0:
    n,x=map(int,input().split())
    if n>5:
        print(math.ceil(n/6)*x)
    else:
        print(n*x)
    t-=1