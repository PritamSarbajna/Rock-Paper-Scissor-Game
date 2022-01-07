import random

user_win = 0;
pc_win = 0;

options = ["rock", "paper", "scissor"]

print("Welcome to the rock, paper, scissors game")
while True:
    user_input = input("Enter Rock / Paper / Scissor or q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        print("Please enter correct input")
        continue
    
    random_num = random.randint(0,2)
    # rock : 0, paper : 1, scissor : 2
    pc_pick = options[random_num]
    
    print("Computer picked", pc_pick)
    
    if user_input == "rock" and pc_pick == "scissor":
        print("You win!")
        user_win += 1
    
    elif user_input == "paper" and pc_pick == "rock":
        print("You win!")
        user_win += 1
    
    elif user_input == "scissor" and pc_pick == "paper":
        print("You win!")
        user_win += 1
    
    elif user_input == pc_pick:
        print("You and computer both have picked same option")
        print("Draw!")
    
    else:
        print("You lost!")
        pc_win += 1
     
print("\nYou won", user_win, "times")
print("Computer won", pc_win, "times")
print("********Thank you for playing the game********")