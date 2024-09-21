import random
user_choice = int(input("enter your choice 0 for Rock 1 for Papper 2 for Scissor :"))
print("computer choice:")
computer_choice = random.randint(0,2)
print(computer_choice)
if computer_choice == user_choice:
    print("It,s a draw")
elif computer_choice ==0 and user_choice==2 :
    print("You lost")
elif computer_choice ==2 and user_choice==0 :
    print("you win")
elif computer_choice > user_choice :
    print("you lost")
elif computer_choice < user_choice :
    print("you win")