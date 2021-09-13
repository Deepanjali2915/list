drivername=("ram","mohan","rahul")
print("Welcome to deeps rides..","\n","How can in i help you.")
print("Where do you want to go?")
currentloaction=input("Enter your current loaction:\n")
droppingpoint=input("Enter your Dropping point:\n")
print("per km price","\n","1km=50rs")
print(drivername)
print("you can choose any one Driver.Because its free:")
choose=input("choose:")
if choose=="ram":
    print("ram age 26:","\n","p.no-1234567890")
elif choose=="mohan" : 
    print("Mohan age 30:","\n","p.no-9876543210")
elif choose=="rahul":
    print("rahul age 22:","\n","p.no-9867542310")
else:
    print("please write only those name:")
    riders=["normal car","bike"]
    print(riders)
    ridername=input("choose any one:")
    if ridername=="bike":
        print("bike colour=black","\n","bike name=TVS","\n","bike no.=DL236")
    elif ridername=="normal car":
        print("car colour=grey","\n","car name=nano","car no.=DL2915")
        print()   
        print("which method you want for paymet.","\n","cash","\n","card")
        payment=("cash and card")
        if payment=="cash":
            print(12345)
        elif payment=="card":
            print(4560)
print("Thank you so much")          
