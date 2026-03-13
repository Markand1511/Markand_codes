def game():

    qna=['\n(1) What Is The Capital Of Bharat ?',
         '\n(2) Which Planet Are Called By "Red Planet"?',
         '\n(3) Who Is Known As The "Father Of The Nation" In Bharat?',
         "\n(4) Which Is The Longest River In The World?",
         "\n(5) Which Is The Highest Mountain In The World?"]

    opt=["[A] Mumbai\n[B] New Delhi\n[C] Ahmadabad \n[D] Bangalore\n",
         "[A] Earth\n[B] Jupiter\n[C] Mars\n[D] Venus\n",
         "[A] Dr. A.P.J. Abdul Kalam\n[B] Mahatma Gandhi\n[C] Sardar Patel\n[D] Bhagat Singh\n",
         "[A] Amazon\n[B] Ganga\n[C] Yangtze\n[D] Nile\n",
         "[A] Kailash\n[B] Kanchenjunga\n[C] Mount Everest\n[D] Nanda Devi\n"]

    ans=['B','C','A','D','C']



    score=0

    for q,o,a in zip(qna,opt,ans):

        print(q,'\n')

        print(o)

        user=input("Enter Your Answer : ").upper()

    
        while user not in ['A','B','C','D']: 
            
            print("Please Type Only Valid Options")

            user=input("Enter Your Answer : ").upper()


        if user==a:

            score+=1000

            print("\nCongratulation Your Answer Is Correct.")

            print(f"Your Score Is :- {score}")


        else:

            print("\nWrong Answer Better Luck Next Time.")

            print(f"Oops! Your Score Is :- {score}")


    print(f"\nNow This Is Your Final Score :- {score}")


    restart=input("Do You Want To Play Again ['Y','N'] : ").upper()


    while restart not in ['Y','N']:

        print("Please Type Only Y Or N ")

        restart=input("Do You Want To Play Again ['Y','N'] : ").upper()
        

    if restart=='Y':

        game()

    elif restart=='N':

        print(f"Good Process You Literally Scored :- {score}, Have A Good Day")
        

game()