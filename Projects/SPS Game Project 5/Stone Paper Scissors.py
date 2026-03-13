import random

import time

opt=['STONE','PAPER','SCISSOR']


User_Score=0

Computer_Score=0


while True:

    print("\n\nType Q for Exit")

    print(f"\nSelect Your Option Like {opt}")

    user=input("\nNow Select Your Option : ").upper()

    if user == 'Q':

        break


    while user not in opt:

        print("\nPlease Enter Right Choice.")

        user=input("\nEnter Your Selection : ").upper()

    
    computer=random.choice(opt)

    time.sleep(1)

    print(f"\nYou Just Selected ['{user}'] and Computer Selected ['{computer}']")


    if user==computer:

        print("\nGAME TIE")

        time.sleep(0.5)

        print(f"\nYou :- {User_Score}  Computer :- {Computer_Score}")



    elif user == 'STONE' and computer =='PAPER':

        time.sleep(0.5)

        print("\nComputer Win And User Lose")

        Computer_Score+=1

        time.sleep(0.5)

        print(f"\nYou :- {User_Score}  Computer :- {Computer_Score}")


    elif user =='STONE' and computer == 'SCISSOR':

        time.sleep(0.5)

        print("\nYou Win And Computer Lose")

        User_Score+=1

        time.sleep(0.5)

        print(f"\nYou :- {User_Score}  Computer :- {Computer_Score}")



    elif user == 'PAPER' and computer == "STONE":

        time.sleep(0.5)

        print("\nYou Win And Computer Lose")

        User_Score+=1

        time.sleep(0.5)

        print(f"\nYou :- {User_Score}  Computer :- {Computer_Score}")


    elif user == 'PAPER' and computer == "SCISSOR":

        time.sleep(0.5)

        print("\nYou Lose And Computer Win")

        Computer_Score+=1

        time.sleep(0.5)

        print(f"\nYou :- {User_Score}  Computer :- {Computer_Score}")


    elif user == 'SCISSOR' and computer == 'STONE':

        time.sleep(0.5)

        print("\nYou Lose And Computer Win")

        Computer_Score+=1

        time.sleep(0.5)

        print(f"\nYou :- {User_Score}  Computer :- {Computer_Score}")


    elif user == 'SCISSOR' and computer == 'PAPER':

        time.sleep(0.5)

        print("\nYou Win And Computer Lose")

        User_Score+=1

        time.sleep(0.5)

        print(f"\nYou :- {User_Score}  Computer :- {Computer_Score}")