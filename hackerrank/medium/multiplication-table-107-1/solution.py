# Enter your code here. Read input from STDIN. Print output to STDOUT
sentence=input()
n=int(sentence.split()[-1])
for i in range(1,11):
    print(n, "x", i ,"=" ,n*i)
