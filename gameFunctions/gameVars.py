from random import randint

choices=["rock", "paper", "scissors"]

#ADDING LIVES-> when one or the other gets to 0, win/ lose
player_lives = 5
computer_lives = 5

total_lives = 5

line= "--------------------------------"

#COMPUTER MAKES CHOICE
computer=choices[randint(0,2)]

#SET UP GAME LOOP HERE
player= False 