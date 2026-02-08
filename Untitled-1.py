def write(user):
    with open("file.txt","w") as f:
        user=input("\nwrite something you want to store inside your file  : ")
        f.write(user)

def read(user):
    with open("file.txt","r") as f:
        print(f.read(user))

def update(user):
    with open("file.txt","a") as f:
        user=input("ok so update your file information something you want : ")
        f.write(user)

def delete():
    with open("file.txt","w") as f:
        f.close()

while True:

    print("\nchoices for operation \n1 for write mode \n2 for read mode \n3 for update mode \n4 for delete file mode : ")
    
    try:
        ch=int(input("now enter your choice for operation : "))

    except ValueError:
        print("only type number between 1 to 4")

        if ch==1:
            write(user)
            print("\ndone")

        elif ch==2:
            read(user)

        elif ch==3:
            update(user)

        else:
            delete()




