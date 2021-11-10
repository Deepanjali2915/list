
# i=int(input("Enter the number: "))
# a=0
# b=0
# while i>0:
#     c=i//10
#     d=i%10
#     a=a + d*2**b
#     b +=1
#     i=c
# print("Decimal number is",a)      


# a=[]
# s=0
# b=0
# size=int(input("Enter the size: "))
# for i in range(size):
#     binary=int(input("Enter the number: "))
#     a.append(binary)
#     while len(a)>0:
#         c=a//10
#         d=a%10
#         a=a+d*2**s
#         s+=1
#         a=c
#     print("Decimai",a)    

a=[1,1,1,1,1,0,1]
i=0
count=0
while 0<len(a):
    # count=count+2**2*1-0*a[-i-1]
    count=(2**i*a)[i-1]
    i=i+1
print(count)


# a=[1,1,1,1,1,0,1,1]
# i=0
# sum=0
# sum1=0
# number=6
# while i<len(a):
#     b=a[number]
#     sum=(2**i*b)
#     number-=1
#     i+=1
#     sum1+=sum
# print(sum1)    
