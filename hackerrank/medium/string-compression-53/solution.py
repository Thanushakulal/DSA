# Enter your code here. Read input from STDIN. Print output to STDOUT
s=input()
realstring=""
for i in s:
    if i not in realstring:
        count=s.count(i)
        if count>1:
            realstring+=i+str(count)
        else:
            realstring+=i
print(realstring)
