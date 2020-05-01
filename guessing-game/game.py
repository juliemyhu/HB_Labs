
import random 

number = random.randint(1,100)
print ("Hola")

player_name = input("Whats your name? ")
player_name = player_name.title()

print ( "Hi {}, I'm thinking of a number between 1 and 100. Try to guess my number ! ".format (player_name))

count = 0
while True:
	try:
		guess = int( input ("Your guess?: "))
		if guess > 100 or guess < 1:
			print ("Silly child, that's not even between 1 and 100. Let's put in a real guess.")
		elif guess > number:
			print ("Your guess is too high, try again.")
			count += 1
		elif guess < number:
			print ("Your guess in too low, try again.")
			count += 1
		else:
			count += 1
			print ("Well done, {} ! You found my number in {} tries ".format(player_name,count))
			break 
	except ValueError:
		print("Thats not a number...")
