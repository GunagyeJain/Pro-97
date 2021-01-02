import random

lowerNumber = int(input("Enter Lower bound:- ")) 

upperNumber = int(input("Enter Upper bound:- ")) 



x = random.randint(lowerNumber, upperNumber)
count = 0
while count<5:
	guess = int(input("Guess a number:- "))

	if x == guess: 
		print("Congratulations you won!")
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")
