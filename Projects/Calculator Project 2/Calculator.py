def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def mod(a,b):
    return a%b

def div(a,b):
    return a/b

def square(user):
    return user*user

def fact(user):

    fact=1
    for i in range(1,user+1):
        fact=fact*i
    return fact

def restart(): 

    while True:

        try:
            
            user=float(input("\nEnter Your First Number : "))

        except ValueError:

            print("\nOther Letters Are Not Allow For Operation Please Enter Digits Only ")
            continue 

        
        print("\n press 1 for +")
        print(" press 2 for -")
        print(" press 3 for *")
        print(" press 4 for %")
        print(" press 5 for /")
        print(" press 6 for square")
        print(" press 7 for fact")


        while True:

            try:

                choice=int(input("\nEnter Your Choice For Operation : "))

                if choice>1 and choice<7:
                    breakpoint

                else:
                    
                    while choice<1 or choice>7:

                        print("\nPlease Enter Right Operation For Calculating")
                        choice=int(input("\nEnter Your Choice For Operation : "))


                if choice==6:

                    print("\nYour Answer Is : ",square(user),"Thank you\n")
                    restart()
                
                if choice==7:

                    print("\nYour Answer Is : ",fact(int(user)),"Thank you\n")
                    restart()


                
            except ValueError:

                    print("\nOther keys Are Not Allow For Operation Please Enter Right Keys Only")
                    continue



            while True:
                
                try:

                    user1=float(input(f"\nYour First Number Is {[user]} Now Please Enter Your Second Number : "))

                except ValueError:

                    print("\nOther Letters Are Not Allow For Operation Please Enter Digits Only ")
                    continue

                
                if choice==1:

                    print("\nYour Answer Is : ",add(user,user1)," Thank you\n")
                    restart()

                elif choice==2:

                    print("\nYour Answer Is : ",sub(user,user1),"Thank you\n")
                    restart()

                elif choice==3:

                    print("\nYour Answer Is : ",multi(user,user1),"Thank you\n")
                    restart()

                elif choice==4:

                    print("\nYour Answer Is : ",mod(user,user1),"Thank you\n")
                    restart()

                elif choice==5:

                    print("\nYour Answer Is : ",div(user,user1),"Thank you\n")
                    restart()
                    
restart()         