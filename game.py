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
		print("tie, no one wins! try again")
	elif player == "quit":
		print("you choose to quit, quitter.")
		exit()
	else:
		print("Not a tie. oh snap")
		if player == "rock":
			print("check and see what the computer is, and win or lose")

	player = False
	computer = choices[randint(0,2)]

