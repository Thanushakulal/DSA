# cook your dish here
p1,p2,p3,p4=map(int,input().split())
arr=p1,p2,p3,p4
len=len(arr)
greaterthan10=0
for i in range(0,len):
    if arr[i]>=10:
        greaterthan10+=1
        i-=1
    else:
        i-=1
print(greaterthan10)