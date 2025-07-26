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
---'    ____)____
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

game = [rock, paper, scissors]
users = int(input("What do you choose? Type 0 for Rock, Type 1 for Paper or Type 2 for Scissors! "))
user_choice = game[users]
print(user_choice)

print("Computer Chose: ")
computer_choice = random.choice(game)
print(computer_choice)

if user_choice == rock and computer_choice == scissors:
    print("You Won!")
elif user_choice == rock and computer_choice == paper:
    print("You Loss")
elif user_choice == paper and computer_choice == rock:
    print("You Won!")
elif user_choice == paper and computer_choice == scissors:
    print("You Loss")
elif user_choice == scissors and computer_choice == paper:
    print("You Won!")
elif user_choice == scissors and computer_choice == rock:
    print("You Loss")
else:
    print("It's a Draw!")
