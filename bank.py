class bank:

    def __init__(self,num,balance):

        self.num=num
        self.balance=balance
    
    def deposit(self,money):

        try:

            if money>=100 and money<=10000:
                self.balance+=money

            else:
                print("your deposit value are low")

        except ValueError:

            print("enter only numbers ")


    def withdraw(self,money):
        
        if money<=self.balance and money>=100 and money<=10000:
            print('\nyour withdraw value are under your balance\n')

            self.balance-=money

        else:
            print("\nyour withdraw value are not match with your balance")
    
    def get_value(self):
        return self.balance
    
obj=bank(9558228763,25000)

try:
    user=float(input('enter your deposit value : '))
    obj.deposit(user)
    print(f'\nyou just deposited {user} in your bank ')
    print('\nthis is your total bank balance after your deposit : ',obj.get_value())

    user=float(input('\nenter your withdraw value : '))
    obj.withdraw(user)
    print(f'\nyou just withdraw {user} in your bank')
    print('\nthis is your total bank balance after your withdraw : ',obj.get_value())

except ValueError:
    print("type only numbers ")