# cook your dish here
t=int(input())
while t>0:
    n=int(input())
    difficulty=map(int,input().split())
    count=0
    for i in difficulty:
        if i>=1000:
            count+=1
            i+=1
        else:
            i+=1
    print(count)
    t-=1