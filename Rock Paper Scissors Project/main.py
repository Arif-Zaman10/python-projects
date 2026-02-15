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

game = ["rock","paper","scissors"]
randon_number = random.randint(0,2)
computer_choose = game[randon_number]


i_choose = input("enter 0 for rock, 1 for paper, 2 for scissors: ")
if i_choose=="0":
    print(f"you choose:\n{rock}")
    print(f"computer choose {computer_choose}")
    if computer_choose=="rock":
        print("It's a tie")
    elif computer_choose=="paper":
        print("You lost")
    elif computer_choose == "scissors":
        print("You won!")
elif i_choose=="1":
    print(f"You choose paper")
    print(f"computer choose {computer_choose}")
    if computer_choose=="rock":
        print("You won!")
    elif computer_choose=="paper":
        print("It's a tie")
    elif computer_choose == "scissors":
        print("You lost")
elif i_choose=="2":
    print(f"You choose scissors")
    print(f"computer choose {computer_choose}")
    if computer_choose=="rock":
        print("You lost")
    elif computer_choose=="paper":
        print("You won!")
    elif computer_choose == "scissors":
        print("It's a tie")
