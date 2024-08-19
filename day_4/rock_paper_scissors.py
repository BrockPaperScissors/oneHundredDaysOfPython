import random

paper = ['''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''', "paper"]

rock = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''', "rock"]

scissors = ['''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''', "scissors"]

rps = [rock, paper, scissors]

player_choice = (int(input("Pick a number, 1. rock, 2. paper, 3. scissors ")) - 1)
computer_choice = random.randint(0, 2)

if player_choice >= 0 and player_choice <= 2:
    print(rps[player_choice][0], f"You have chosen {rps[player_choice][1]} ")
    print(rps[computer_choice][0], f"The computer has chosen {rps[computer_choice][1]}")

    if player_choice == 0:
        if computer_choice == 0:
            print("\nIt's a tie!")
        elif computer_choice == 1:
            print("\nThe computer wins!")
        elif computer_choice == 2:
            print("\nYou win!")
    elif player_choice == 1:
        if computer_choice == 1:
            print("\nIt's a tie!")
        elif computer_choice == 2:
            print("\nThe computer wins!")
        elif computer_choice == 0:
            print("\nYou win!")
    elif player_choice == 2:
        if computer_choice == 2:
            print("\nIt's a tie!")
        elif computer_choice == 0:
            print("\nThe computer wins!")
        elif computer_choice == 1:
            print("\nYou win!")
else:
    print("Please enter a valid number.")