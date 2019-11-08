from random import randint
from gameFunctions import gameVars

def winorlose(status):
	print(gameVars.line)
	print("You", status, "Would you like to play again?")
	choice = input("Y / N ?")

	#RESET GAME
	if choice == "Y" or choice == "y":
		gameVars.player_lives = 5
		gameVars.computer_lives = 5
		gameVars.player = False
		gameVars.computer = gameVars.choices[randint(0, 2)]

	#QUIT GAME
	elif choice == "N" or choice == "n":
		print("You choose to quit. Better luck next time.")
		exit()

	#NOT VALID ANSWER
	else:
		print("Make a valid choice Yes or No")
		winorlose(status)