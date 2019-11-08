from gameFunctions import gameVars

def compare(player):
	#TIE GAME
	if player == gameVars.computer:
		print(gameVars.space)
		print(gameVars.arrow)
		print(gameVars.space)
		print("Tie, no one wins! Try again.\n")
		print(gameVars.equal)
	#PLAYER == QUIT
	elif player == "quit":
		print(gameVars.space)
		print(gameVars.arrow)
		print(gameVars.space)
		print("You choose to quit. See you again soon.\n")
		exit()

	#PLAYER == ROCK
	elif player == "rock": 
		if gameVars.computer == "paper":
			print(gameVars.space)
			print(gameVars.arrow)
			print(gameVars.space)
			print("You lose!", gameVars.computer, "covers", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
			print(gameVars.equal)
		else:
			print(gameVars.space)
			print(gameVars.arrow)
			print(gameVars.space)
			print("You won!", player, "smashes", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1
			print(gameVars.equal)

	#PLAYER == PAPER
	elif player == "paper": 
		if gameVars.computer == "scissors":
			print(gameVars.space)
			print(gameVars.arrow)
			print(gameVars.space)
			print("You lose!", gameVars.computer, "cuts", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
			print(gameVars.equal)
		else:
			print(gameVars.space)
			print(gameVars.arrow)
			print(gameVars.space)
			print("You won!", player, "covers", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1
			print(gameVars.equal)

	#PLAYER == SCISSORS
	elif player == "scissors": 
		if gameVars.computer == "rock":
			print(gameVars.space)
			print(gameVars.arrow)
			print(gameVars.space)
			print("You lose!", gameVars.computer, "smashes", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
			print(gameVars.equal)
		else:
			print(gameVars.space)
			print(gameVars.arrow)
			print(gameVars.space)
			print("You won!", player, "cuts", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1
			print(gameVars.equal)


