# cook your dish here
t=int(input())
while t>0:
    rev=0
    n=int(input())
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    print(rev)
    t-=1