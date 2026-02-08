class bank:

    def __init__(self,num,balance):

        self.num=num
        self.balance=balance
    
    def deposit(self,money):

        try:

            if money>=100 and money<10000:
                self.balance+=money

            else:
                print("\nenter right amount for deposit a money and your bank balance are same as previous total bank balance ")


        except ValueError:

            print("enter only numbers ")


    def withdraw(self,money):
        
        if money<self.balance and money>=100 and money<=10000:
            print('\nyour withdraw value are under your balance\n')

            self.balance-=money

        else:
            print("\nyour withdraw value are not match with your balance so your bank balance are same as previous total bank balance ")
        

    def get_value(self):
        return self.balance
    
obj=bank(9558228763,25000)
obj2=bank(9558228764,50000)

while True:
    try:
        user=float(input('\nenter your deposit value : '))
        obj.deposit(user)
        print(f'\nyou just deposited {user} in your bank ')
        print('\nthis is your total bank balance after your deposit : ',obj.get_value())

        user=float(input('\nenter your withdraw value : '))
        obj.withdraw(user)
        print(f'\nyou just withdraw {user} in your bank')
        print('\nthis is your total bank balance after your withdraw : ',obj.get_value())



        user2=float(input('\nenter your deposit value : '))
        obj2.deposit(user2)
        print(f'\nyou just deposited {user2} in your bank ')
        print('\nthis is your total bank balance after your deposit : ',obj2.get_value())

        user2=float(input('\nenter your withdraw value : '))
        obj2.withdraw(user2)
        print(f'\nyou just withdraw {user2} in your bank')
        print('\nthis is your total bank balance after your withdraw : ',obj2.get_value())

    except ValueError:
        print("\ntype only numbers ")