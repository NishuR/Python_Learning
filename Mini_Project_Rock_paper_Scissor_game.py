import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_image = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor : "))
print(game_image[user_choice])
computer_random = random.randint(0, 2)
print("Computer Chose :")
print(game_image[computer_random])
if user_choice >= 3 or user_choice < 0:
    print("Choose correct number for game : ")
elif user_choice == 0 and computer_random == 2:
    print("You win!!")
elif computer_random == 0 and user_choice == 2:
    print("You win!!")
elif computer_random > user_choice:
    print("You lose!!")
elif computer_random < user_choice:
    print("You win!!")
elif computer_random == user_choice:
    print("It's a draw. Play again.")

