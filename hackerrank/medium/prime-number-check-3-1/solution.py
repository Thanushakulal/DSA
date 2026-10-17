# Enter your code here. Read input from STDIN. Print output to S
n=int(input())
isprime=True
if n<=1:
    isprime=False
else:
    for i in range(2,n):
        if n%i==0:
            isprime=False
            break
        else:
            isprime=True
if isprime:
    print("yes")
else:
    print("no")
