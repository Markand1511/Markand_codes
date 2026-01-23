def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):

    if a and b==0:
        print("invalid number")

    else:
        return a/b
    
while True:

    user=int(input("\n enter your first number : "))

    print("\n press 1 for +")
    print("\n press 2 for -")
    print("\n press 3 for *")
    print("\n press 4 for /")

    choise=int(input("\n enter your choise for operation : "))

    user1=int(input("\n enter your second number : "))
    

    if choise==1:
        print(" your answer is : ",add(user,user1))

    elif choise==2:
        print(" your answer is : ",sub(user,user1))

    elif choise==3:
        print(" your answer is : ",multi(user,user1))
    
    else:
        print(" your answer is : ",div(user,user1))