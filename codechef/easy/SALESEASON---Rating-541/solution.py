# cook your dish here
t=int(input())
while t>0:
    x=int(input())
    if x<=100:
        print(x)
    elif 100<x<=1000:
        print(x-25)
    elif 1000<x<=5000:
        print(x-100)
    else:
        print(x-500)
    t-=1