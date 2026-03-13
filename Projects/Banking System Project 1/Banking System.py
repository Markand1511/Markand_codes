class bank:

    def __init__(self,balance):

        self.balance=balance
    
    def deposit(self,user_amount):

        self.balance+=user_amount
    
    def withdraw(self,user_amount):

        self.balance-=user_amount
            
    def get_value(self):

        return self.balance


# OBJECT 1

obj=bank(25000)

# DEPOSIT PROCESS OF OBJECT 1

while True:

    try:
        
        user_amount=int(input('\n[Object_1] Enter Your Deposit Value Here : '))

    except :

        print("\nIt Is Invalid Key So Please Enter Right Details For Your Bank Account.")

        continue

    
    if 100 < user_amount < 10000:

        obj.deposit(user_amount)
        
        print(f'\n\nYou Just Deposited {user_amount} To Your Bank Account.')

        print('\nThis Is Your Total Bank Balance After Your Deposit : ',obj.get_value())

    else:
                
        if user_amount < 100:

            print("\n\nYour Deposit Amount Are To Low.")

            print("\nNow This Is Your Total Bank Balance : ",obj.get_value())


        elif user_amount > 10000:

            print("\n\nYour Deposit Amount Are To High.")

            print("\nNow This Is Your Total Bank Balance :",obj.get_value())


# WITHDRAW SELECTION  PROCESS OF OBJECT 1


    choice=str(input("\n\nDo you Want To Withdraw Your Money [Y/N] : ")).upper()

    while choice not in ['Y','N']:

        print("\nAnswer Only In [Y/N].")

        choice=str(input("\nDo you Want To Withdraw Your Money [Y/N] : ")).upper()

    if choice=="N":

        print("\n\nOk So This Is Your Total Bank Balance After Your Deposit : ",obj.get_value())

        print("\nThank You , Have A Good Day \n")

        

# WITHDRAW PROCESS OF OBJECT 1


    if choice=="Y":

        while True:

            try:
    
                user_amount=float(input('\n\n[Object_1] Enter Your Withdraw Value Here : '))

            except :

                print("\nIt Is Invalid Key So Please Enter Right Details For Your Bank Account.")

                continue
            
        

            if 100 < user_amount < 10000 and user_amount < obj.get_value():

                obj.withdraw(user_amount)

                print(f'\n\nYou Just withdraw {user_amount} From Your Bank Account.')

                print("\nThis Is Your Total Bank Balance After Your Withdraw : ",obj.get_value())
            
            else:

                if user_amount < 100:

                    print("\n\nYour Withdraw Amount Are To Low.")

                    print("\nNow This Is Your Total Bank Balance : ",obj.get_value())

                    
                elif user_amount > 10000:

                    print("\n\nYour withdraw Amount Are To High.")

                    print("\nNow This Is Your Total Bank Balance :",obj.get_value)

                    
# OBJECT 2

            obj2=bank(50000)


# DEPOSIT  PROCESS OF OBJECT 2


            while True:

                try:

                    user_amount2=float(input('\n\n[object_2] Enter Your Deposit Value Here : '))

                except :

                    print("\nIt Is Invalid Key So Please Enter Right Details For Your Bank Account.")

                    continue


                if 100 < user_amount2 < 10000:

                    obj2.deposit(user_amount2)

                    print(f'\n\nYou Just Deposited {user_amount2} To Your Bank Account.')

                    print('\nThis Is Your Total Bank Balance After Your Deposit : ',obj2.get_value())

                else:

                    if user_amount2 < 100:

                        print("\n\nYour Deposit Amount Are To Low.")

                        print("\nNow This Is Your Total Bank Balance : ",obj2.get_value())


                    elif user_amount2 > 10000:

                        print("\n\nYour Deposit Amount Are To High.")

                        print("\nNow This Is Your Total Bank Balance :",obj2.get_value())



# WITHDRAW SELECTION  PROCESS OF OBJECT 2


                choice=str(input("\n\nDo you Want To Withdraw Your Money [Y/N] : ")).upper()

                while choice not in ['Y','N']:

                    print("\nAnswer Only In [Y/N].")

                    choice=str(input("\nDo you Want To Withdraw Your Money [Y/N] : ")).upper()

                if choice=="N":

                        print("\n\nOk So This Is Your Total Bank Balance After Your Deposit : ",obj2.get_value())

                        print("\nThank You , Have A Good Day \n")

                        

# WITHDRAW PROCESS OF OBJECT 2


                if choice=="Y":

                    while True:

                        try:

                            user_amount2=float(input('\n\n[Object_2] Enter Your Withdraw Value Here : '))

                        except :

                            print("\nIt Is Invalid Key So Please Enter Right Details For Your Bank Account.")

                            continue


                        if 100 < user_amount2 < 10000 and user_amount2 < obj2.get_value():

                            obj2.withdraw(user_amount2)

                            print(f'\n\nYou Just withdraw {user_amount2} From Your Bank Account.')

                            print("\nThis Is Your Total Bank Balance After Your Withdraw : ",obj2.get_value())

                        else:

                            if user_amount2 < 100:

                                print("\n\nYour Withdraw Amount Are To Low.")

                                print("\nNow This Is Your Total Bank Balance : ",obj2.get_value())

                                                             
                            elif user_amount2 > 10000:

                                print("\n\nYour withdraw Amount Are To High.")

                                print("\nNow This Is Your Total Bank Balance :",obj2.get_value())