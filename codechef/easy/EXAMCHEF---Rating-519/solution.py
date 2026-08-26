# cook your dish here
t=int(input())
while t>0:
    x,y,z=map(int,input().split())
    if z > (x*y)/2:
        print("yes")
    else:
        print("no")
    t-=1