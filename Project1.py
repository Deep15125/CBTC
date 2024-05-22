# Author - Deep Gupta
import random

print('Winning rules of the game STONE PAPER SCISSOR are :\n'
      + "Stone vs Paper -> Paper wins \n"
      + "Stone vs Scissor -> Stone wins \n"
      + "Paper vs Scissor -> Scissor wins \n")
print("Author --> Deep Gupta")

while True:

    print("Enter your choice \n 1.-> STONE \n 2.-> Paper \n 3.-> Scissor \n")

    choice = int(input("Enter your choice :"))

    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please '))

    if choice == 1:
        choice_name = 'Stone'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissor'

    print('User choice is \n', choice_name)
    print('Now its Computers Turn....')

    comp_choice = random.randint(1, 3)

    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Stone'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissor'
    print("Computer choice is \n", comp_choice_name)
    print(choice_name, 'Vs', comp_choice_name)

    if choice == comp_choice:
        print('Its a Draw', end="")
        result = "DRAW"

    if (choice == 1 and comp_choice == 2):
        print('paper wins ==', end="")
        result = 'Paper'
    elif (choice == 2 and comp_choice == 1):
        print('paper wins ==', end="")
        result = 'Paper'

    if (choice == 1 and comp_choice == 3):
        print('Stone wins ==', end="")
        result = 'STONE'
    elif (choice == 3 and comp_choice == 1):
        print('Stone wins ==', end="")
        result = 'STONE'

    if (choice == 2 and comp_choice == 3):
        print('Scissor wins ==', end="")
        result = 'SCISSOR'
    elif (choice == 3 and comp_choice == 2):
        print('Scissor wins ==', end="")
        result = 'SCISSOR'

    if result == 'DRAW':
        print("=> Match is DRAW ==>")
    if result == choice_name:
        print("=> You wins ==>")
    else:
        print("= Computer wins ==>")
    print("Do you want to play again? (Y/N)")

    ans = input().lower()
    if ans == 'n':
        break

print("Thanks for Playing STONE, PAPER, SCISSOR")
