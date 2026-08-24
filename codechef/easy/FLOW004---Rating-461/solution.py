# cook your dish here
t=int(input())
while t>0:
    n=input()
    length=len(n)
    sum=int(n[0]) + int(n[length-1])
    print(sum)
    t-=1
    