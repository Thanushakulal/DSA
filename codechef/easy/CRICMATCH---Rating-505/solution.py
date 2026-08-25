# cook your dish here
t=int(input())
while t>0:
    m,n=map(int,input().split())
    if n*6*6>=m: # one over has 6 balls..each ball can have a six
        print("yes") 
    else:
        print("no")
    t-=1