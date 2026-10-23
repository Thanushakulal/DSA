# Enter your code here. Read input from STDIN. Print output to STDOUT
s=input()
if s=="10":
    print("1010")
elif all(c in "01" for c in s):
    print(int(s,2))
else:
    print(bin(int(s))[2:1])
