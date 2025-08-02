# Imported required modules:
import random

# Introduction:
game='''
Game Name: Rock Paper Scissors
Created By: Aaryan Kumar 
'''

# Game Instructions Variable created:
instructions='''
Important Instructions:
1. Choose '1' for 'ROCK'
2. Choose '0' for 'PAPER'
3. Choose '-1' for 'SCISSOR'
4. Rules: Rock beats scissors, scissors beat paper, and paper beats rock.
5. You have to choose your Fininshing point on your own.
6. Player who reaches the 'Finishing Point' first WINS the game.
'''

print("\n",game,"\n")

# Decision to start the game taken by User
start=input("\nDo you want to start the GAME [yes/no]: ")

# Game Algorithm
while(start=="yes"):

    # Printing Introduction:
    print("\n$~~~~~~~~~~~~~~~~~~~~ WELCOME TO THE GAME ~~~~~~~~~~~~~~~~~~~~~~$")
    print("\n",instructions,"\n")

    # Finishing Points choice taken by User:
    n=int(input("Enter the Finishing point: "))

    # Initiating variables:
    points_of_computer=0
    points_of_user=0
    list=[1,0,-1]
    dictionary={1:"ROCK",0:"PAPER",-1:"SCISSOR"}

    print("\nGame Started...!")

    # Game Logic:
    while(points_of_computer<n or points_of_user<n):

        user=int(input("\nEnter your Choice: "))
        user_choice=dictionary[user]
        comp=random.choice(list)
        comp_choice=dictionary[comp]

        if comp == user:
            print("\nComputer: ",comp_choice,"\nUser : ",user_choice,"\nIt's a Draw")
            print("\nUser points: ",points_of_user,"\nComputer Points :",points_of_computer)

        elif comp==1 and user==0:
            print("\nComputer: ",comp_choice,"\nUser: ",user_choice,"\nUser win")
            points_of_user += 1
            print("\nUser points: ",points_of_user,"\nComputer Points :",points_of_computer)
            if points_of_user==n:
                print("\n\nUser WON the game...!!\n<<Computer LOST>>")
                break

        elif comp==0 and user==-1:
            print("\nComputer: ",comp_choice,"\nUser: ",user_choice,"\nUser win")
            points_of_user += 1
            print("\nUser points: ",points_of_user,"\nComputer Points :",points_of_computer)
            if points_of_user==n:
                print("\n\nUser WON the game...!!\n<<Computer LOST>>")
                break

        elif comp==-1 and user==1:
            print("\nComputer: ",comp_choice,"\nUser: ",user_choice,"\nUser win")
            points_of_user += 1
            print("\nUser points: ",points_of_user,"\nComputer Points :",points_of_computer)
            if points_of_user==n:
                print("\n\nUser WON the game...!!\n<<Computer LOST>>")
                break

        else:
            print("\nComputer: ",comp_choice,"\nUser: ",user_choice,"\nUser lose")
            points_of_computer += 1
            print("\nUser points: ",points_of_user,"\nComputer Points :",points_of_computer)
            if points_of_computer==n:
                print("\n\nComputer WON the game...!!\n<<User LOST>>")
                break
            
    start=input("\n\nDo you want to play again [yes/no]: ")

else:
    print("\n\nOK...!\nSee you next time.\nHave a great day ahead")