# Enter your code here. Read input from STDIN. Print output to STDOUT
s1=input()
s2=input()
if sorted(s1)==sorted(s2):
    print("Anagrams")
else:
    print("Not Anagrams")
