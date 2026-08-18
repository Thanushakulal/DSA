# cook your dish here
t=int(input())
while (t>0):
    a,b,c=map(int,input().split())
    if (a+b)/2>c:
        print("yes")
    else:
        print("no")
    t-=1
    