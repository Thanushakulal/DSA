# cook your dish here
s=input()
len=len(s)
if s[0]=='c' or s[len-1]=='f' or (s[0]=='c' and s[len-1]=='f'):
    print("yes")
else:
    print("no")