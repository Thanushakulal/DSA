string=input()
rev=""
for i in string:
    rev=i+rev
if string==rev:
    print("Yes")
else:
    print("No")
