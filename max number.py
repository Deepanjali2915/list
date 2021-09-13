
# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# max=numbers[0]
# for i in numbers:
#     if i>max:
#         max=i
# print(max)


numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
max=numbers[0]
while i<len(numbers): 
    if numbers[i]<max:
        max=numbers[i]
    i+=1
print(max) 
         


# student_marks = [23, 45, 89, 90, 56, 80] 
# length = len(student_marks)
# index = 0
# total_marks = 0
# while index < len(student_marks):
#     total_marks = student_marks[index] + total_marks
#     index = index + 1
# print ("Total Marks: " + str(total_marks))
