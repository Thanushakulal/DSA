# Enter your code here. Read input from STDIN. Print output to STDOUT
a,b=map(int,input().split())
x,y=a,b
while b!=0:
    a,b=b,a%b
gcd=a
lcm=x*y//gcd
print(f"GCD of {x} and {y} is {gcd} ")
print(f"LCM of {x} and {y} is {lcm}")
