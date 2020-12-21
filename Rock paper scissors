import random

permitted_word = ["rock", "r", "paper", "p", "scissors", "s"]
computer_permitted_word = ["rock", "paper", "scissors"]
user_wins = 0
computer_wins = 0
while True:
    users_answer = input("Please select between rock, paper, or scissors: ")
    while users_answer not in permitted_word:
        users_answer = input("Invalid Answer. Please ONLY select between rock, paper, or scissors: ")

    com_answer = random.choice(computer_permitted_word)
    print("Computer's Answer: " , com_answer)
    if (((users_answer == "paper" or users_answer == "p") and com_answer == "rock" ) or \
        ((users_answer == "rock" or users_answer == "r") and com_answer == "scissors" )  or \
        ((users_answer == "scissors" or users_answer == "s" ) and com_answer == "paper" )):
        user_wins += 1
        print ("You win! \nYou Won {} times and Computer Won {} times".format(user_wins,computer_wins))
    elif (((users_answer == "rock" or users_answer == "r" ) and com_answer == "paper" ) or \
          ((users_answer == "paper" or users_answer == "p") and com_answer == "scissors" ) or \
          ((users_answer == "scissors" or users_answer == "s") and com_answer == "rock" )):
          computer_wins += 1
          print ("You lose! \nYou Won {} times and Computer Won {} times".format(user_wins,computer_wins))
    else:
        print ("It's a tie!!")
    
    repeat = input("Play again? (Y/N) ")
    while repeat not in ['y', 'n']:
        repeat = input("That is not a valid choice. Please try again: ")
    if repeat == 'n':
        break
    print("\n----------------------------\n")
