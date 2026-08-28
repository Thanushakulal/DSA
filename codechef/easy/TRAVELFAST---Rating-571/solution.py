# cook your dish here
t=int(input())
while t>0:
    x,y=map(int,input().split())
    if x==y:
        print("SAME")
    elif x<y:
        print("BIKE")
    else:
        print("CAR")
    t-=1