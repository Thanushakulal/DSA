# cook your dish here
l,r=map(int,input().split())
even=False
for i in range(l,r+1,1):
    if i%2==0:
        even=True
        break
    else:
        even=False
if even:
    print("yes")
else:
    print("no")
