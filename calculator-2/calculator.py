"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


while True:
	input_string = input("Enter your equation: ")
	token = input_string.split()
	print (token)

	token[1] = float(token[1])
	token[2] = float(token[2])

	answer = None

	if "q" in token:
		print ("calculator shutting down...")
		break 

	elif token[0] == "+":
		answer = add(token[1],token[2])

	elif token[0] == "-":
		answer = subtract(token[1], token[2])
	# pow 3 9 
	elif token[0] == "*":
		answer = multiply(token[1], token[2])

	elif token[0] == "/":
		answer = divide(token[1], token[2])

	elif token[0] == "square":
		answer = square(token[1])

	elif token[0] == "cube":
		answer = cube(token[1])

	elif token[0] == "pow":
		answer = power(token[1], token[2])

	elif token[0] == "mod" or token[0] == "%":
		answer = mod(token[1], token[2])


	print(answer)
