#import the random package so we can generate a random AI choice from random import randint 
from random import randint
from gameFunctions import winlose, gameVars, compare

while gameVars.player is False:
	print("================================\n")
	print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
	print("\n================================")
	print("Choose your weapon!")
	print(gameVars.line)
	player=input ("Choose rock, paper or scissors: \n") 

	#print("computer:", computer, "player", player)

	compare.compare(player)

	#PLAYER LOST
	if gameVars.player_lives == 0:
		winlose.winorlose("lost.")
			
	#PLAYER WON
	elif gameVars.computer_lives == 0:
		winlose.winorlose("win.")
	
	#GAME LOOP	
	else:
		compare.player = False
		gameVars.computer = gameVars.choices[randint(0,2)]

