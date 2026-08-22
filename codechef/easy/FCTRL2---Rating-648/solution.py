# cook your dish here
t=int(input())
while t>0:
    n=int(input())
    fact=1
    while n>0:
        fact=fact*n
        n-=1
    print(fact)
    t-=1