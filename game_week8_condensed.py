#import the random package so we can generate a random AI choicefrom random import randint 
from random import randint

#"basket" of choices
choices=["rock", "paper", "scissors"]

#adding lives -> when one or the other gets to 0, win/ lose
player_lives = 5
computer_lives = 5

# let the AI make a choice
computer=choices[randint(0,2)]

#set up a game loop here so we dont have to keep restarting
player= False 

def winorlose(status):
	# print("called win or lose function", status, "\n")
	print("You", status, "Would you like to play again?")
	choice = input("Y / N ?")

	if choice == "Y" or choice == "y":
		global player_lives
		global computer_lives
		global player
		global computer
		#reset the game and start all over again
		player_lives = 5
		computer_lives = 5
		player = False
		computer = choices[randint(0,2)]

	elif choice == "N" or choice == "n":
		print("You choose to quit. Better luck next time.")
		exit()

	else:
		print("Make a valid choice Yes or No")

while player is False:
	print("======================================")
	print("computer lives:", computer_lives, "/5\n")
	print("player lives:", player_lives, "/5\n")
	print("======================================")
	print("Choose your Weapon!\n")
	player=input ("choose rock, paper or scissors: \n") 
	#print(computer, player)

	#start doing some logic and condition checking
	#print("computer:", computer, "player", player)

	#always check a breaking condition first
	if player == computer:
		#we have a tie, no point in going any further
		print("Tie, no one wins! Try again \n")
	elif player == "quit":
		#you quit, lets player exit game
		print("You choose to quit, quitter.\n")
		exit()
	
	#PLAYER == ROCK
	elif player == "rock": 
		if computer == "paper":
			print("You lose!", computer, "covers", player, "\n")
			player_lives = player_lives -1
		else:
			print("You won!", player, "smashes", computer, "\n")
			computer_lives = computer_lives -1
	
	#PLAYER == PAPER
	elif player == "paper": 
		if computer == "scissors":
			print("You lose!", computer, "cuts", player, "\n")
			player_lives = player_lives -1
		else:
			print("You won!", player, "covers", computer, "\n")
			computer_lives = computer_lives -1
	
	#PLAYER == SCISSORS
	elif player == "scissors": 
		if computer == "rock":
			print("You lose!", computer, "smashes", player, "\n")
			player_lives = player_lives -1
		else:
			print("You won!", player, "cuts", computer, "\n")
			computer_lives = computer_lives -1

	if player_lives == 0:
		winorlose("lose")
		# print("You lose. Loser. Would you like to play again?")
		# choice = input("Y / N ?")

		# if choice == "Y" or choice == "y":
		# 	#reset the game and start all over again
		# 	player_lives = 5
		# 	computer_lives = 5
		# 	player = False
		# 	computer = choices[randint(0,2)]
		# elif choice == "N" or choice == "n":
		# 	print("You choose to quit. Better luck next time.")
		# 	exit()
		# else:
		# 	print("Make a valid choice. Yes or No!")
			

	elif computer_lives == 0:
		winorlose("win")
		# print("You Won! Would you like to play again?")
		# choice = input("Y / N ?")

		# if choice == "Y" or choice == "y":
		# 	#reset the game and start all over again
		# 	player_lives = 5
		# 	computer_lives = 5
		# 	player = False
		# 	computer = choices[randint(0,2)]
		# elif choice == "N" or choice == "n":
		# 	print("You choose to quit. Better luck next time.")
		# 	exit()
		# else:
		# 	print("Make a valid choice. Yes or No!")
		# 	choice = input("Y / N ?")

	else:
		player = False
		computer = choices[randint(0,2)]

