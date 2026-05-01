def write(user):

    with open('Projects/CRUD Project 3/My_File.txt','w')as f:

        f.write(user)

def read():

    with open('Projects/CRUD Project 3/My_File.txt','r')as f:

        print(f.read())

def append(user1):

    with open('Projects/CRUD Project 3/My_File.txt','a')as f:

        f.write(user1)

def delete():

    with open('Projects/CRUD Project 3/My_File.txt','w') as f:

        f.close()


while True:

    print("\n1 For Write Mode.\n\n2 For Read Mode.\n\n3 For Append Mode.\n\n4 For Delete Mode.")

    choice=input("\n\nEnter Your Choice : ")


    while choice not in ['1','2','3','4']:

        print('\nInvalid Choice Selection')

        choice=int(input("\n\nEnter Your Choice : "))
        

    if choice=='1':

        user=input("\nEnter Something You Want to Store Inside Your File : ")

        write(user)

        print("\nSuccessfully Added")


    elif choice=='2':

        read()

        
    elif choice=='3':

        user1=input("\nOk So Enter Something You Want to Add Inside Your File : ")

        print("\nSuccessfully Added")

        append(user1)


    elif choice=='4':

        print("\nYour File Data Are Deleted Successfully")

        delete()