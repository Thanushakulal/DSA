# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    counteven=0
    countodd=0
    
    for i in range(1,n+1):
        if n%i==0:
            if i%2==0:
                counteven+=1
            else:
                countodd+=1
            i+=1
    print(countodd,counteven)