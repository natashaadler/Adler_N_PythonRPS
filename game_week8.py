#import the random package so we can generate a random AI choicefrom random import randint 
from random import randint

#"basket" of choices
choices=["rock", "paper", "scissors"]

# let the AI make a choice
computer=choices[randint(0,2)]

#set up a game loop here so we dont have to keep restarting
player= False 

while player is False:
	player=input ("choose rock, paper or scissors: \n") 
	#print(computer, player)

	#start doing some logic and condition checking
	print("computer:", computer, "player", player)

	#always check a breaking condition first
	if player == computer:
		#we have a tie, no point in going any further
		print("Tie, no one wins! Try again")
	elif player == "quit":
		#you quit, lets player exit game
		print("You choose to quit, quitter.")
		exit()
	#PLAYER == ROCK
	elif player == "rock": 
		if computer == "paper":
			print("You lose!", computer, "covers", player, "\n")
		else:
			print("You won!", player, "smashes", computer, "\n")
	#PLAYER == PAPER
	elif player == "paper": 
		if computer == "scissors":
			print("You lose!", computer, "cuts", player, "\n")
		else:
			print("You won!", player, "covers", computer, "\n")
	#PLAYER == SCISSORS
	elif player == "scissors": 
		if computer == "rock":
			print("You lose!", computer, "smashes", player, "\n")
		else:
			print("You won!", player, "cuts", computer, "\n")

	player = False
	computer = choices[randint(0,2)]

