def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):

    if a or b==0:
        print("invalid number")

    else:
        return a/b
    
while True:
    try:
        user=int(input("\n enter your first number : "))

    except ValueError:
        print("\nother letters are not allow for operation please enter digits only ")   
        
        print("\n press 1 for +")
        print("press 2 for -")
        print("press 3 for *")
        print("press 4 for /")
        
    try:
        choice=int(input("\n enter your choice for operation : "))

        user1=int(input(f"\n your first number is {[user]} now please enter your second number : "))

    except ValueError:
        print("\nother letters are not allow for operation please enter digits only ")   
        
    
        if choice==1:
            print(" your answer is : ",add(user,user1))

        elif choice==2:
            print(" your answer is : ",sub(user,user1))

        elif choice==3:
            print(" your answer is : ",multi(user,user1))
    
        else:
            print(" your answer is : ",div(user,user1))

    