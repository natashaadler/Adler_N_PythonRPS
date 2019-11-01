#import the random package so we can generate a random AI choicefrom random import randint 
from random import randint


choices =["rock", "paper", "scissors"]
computer = choices[randint(0,2)]
lives = 5
player = False
line = ''' ----------------- '''


while player is False:

	player = input ("Choose rock, paper or scissors: ") 
	#print(computer, player)

	#player winner screen
	player_winner_screen = f'''

	{line}

	 Player Wins!!!

	 {player} beats {computer}
	 Type rock, paper, scissors to play again!

	{line}

	'''

	#computer winner screen
	computer_winner_screen = f'''
	
	{line}

	 Computer Wins!!!
	
	{computer} beats {player}

	{line}
	'''

	#determines wether its a draw
	if player == computer:
		print(f'''
		{line}

		Its a DRAW!
		{computer} = {player}
		Type rock, paper, scissors to play again!

		{line}
		''')
	#if the player trys to quit it will exit the program
	elif player == "quit":
		print("you choose to quit, quitter.")
		exit()

	else:
		
		#check who wins
		if player == "rock" and computer == "paper":
			print(computer_winner_screen)

		elif player == "paper" and computer == "rock":
			print(player_winner_screen)

		elif player == "paper" and computer == "scissors":
			print(computer_winner_screen)

		elif player == "scissors" and computer == "paper":
			print(player_winner_screen)

		elif player == "scissors" and computer == "rock":
			print(computer_winner_screen)

		elif player == "rock" and computer == "scissors":
			print(player_winner_screen)

		#if not a valid command type:
		else:
			print("Not a valid answer, please retry")
		
	player = False
	computer = choices[randint(0,2)]

