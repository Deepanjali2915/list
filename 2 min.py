numbers = [80, 40, 23, 100, 90, 10, 7]
i=0
minfirst=numbers[0]
minsecond=numbers[0]
while i<len(numbers): 
    if numbers[i]>minfirst:
        minfirst=numbers[i]
    elif numbers[i]>minsecond and numbers[i]<minfirst:
        minsecond=numbers[i]    
    i+=1
print(minfirst)    
print(minsecond)






