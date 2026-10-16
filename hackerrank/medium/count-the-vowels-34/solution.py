# Enter your code here. Read input from STDIN. Print output to STDOUT
s=input()
count=0
for i in s:
    if i in "aeiou":
        count+=1
print(count)
