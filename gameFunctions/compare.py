from gameFunctions import gameVars

def compare(player):
	#TIE GAME
	if player == gameVars.computer:
		print("Tie, no one wins! Try again \n")
		print(gameVars.line)
	#PLAYER == QUIT
	elif player == "quit":
		print("You choose to quit. See you again soon.\n")
		exit()

	#PLAYER == ROCK
	elif player == "rock": 
		if gameVars.computer == "paper":
			print("You lose!", gameVars.computer, "covers", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("You won!", player, "smashes", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1

	#PLAYER == PAPER
	elif player == "paper": 
		if gameVars.computer == "scissors":
			print("You lose!", gameVars.computer, "cuts", player, "\n")
		else:
			print("You won!", player, "covers", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1

	#PLAYER == SCISSORS
	elif player == "scissors": 
		if gameVars.computer == "rock":
			print("You lose!", gameVars.computer, "smashes", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("You won!", player, "cuts", computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1


