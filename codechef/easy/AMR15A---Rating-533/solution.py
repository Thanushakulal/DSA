# cook your dish here
n=int(input())
weapons=map(int,input().split())
evencount=0
oddcount=0

for i in weapons:
    if i%2==0:
        evencount+=1
    else:
        oddcount+=1
        
if evencount>oddcount:
    print("READY FOR BATTLE")
else:
    print("NOT READY")