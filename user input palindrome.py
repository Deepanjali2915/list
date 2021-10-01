size=int(input("enter your size:"))
i=0
a=[]
while i <size:
    user=input("enter :")
    a.append(user)
    b=[]
    for j in range(len(a)-1,-1,-1):
        b.append(a[j])
    i+=1
print(a)
print(b)
if b==a:
    print("Palindrome")
else:
    print("not")    
