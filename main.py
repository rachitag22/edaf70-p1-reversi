# Lund University | EDAF70 | Project 1 - Reversi
# Rachit Agarwal | Jay Mangrulkar

import numpy as np

# Creates empty game board
def createEmptyBoard():
	board = []
	size = 8
	for row in range(0,size):
		board.append([])
		for col in range(0,size):
			# * = empty, O = white, X = black
			# O is letter O not 0
			board[row].append("*")
	return board

# Sets up initial game board
def setupBoard():
	board = createEmptyBoard()

	board[3][3] = "O"
	board[4][4] = "O"
	board[3][4] = "X"
	board[4][3] = "X"

	return board


# Prints the game board
def printBoard(board):
	print("Current Board:")
	print np.matrix(board)

# Handles user color selection
def selectColor():
	userColorInput = input("What color would you like to play as? Please enter 'black' or 'white'.")
	if userColorInput = "black":
		userColor = "black"
		cpuColor = "white"
	else:
		userColor = "white"
		cpuColor = "black"

	print("Great! You are playing as %s. The CPU is playing as %s.", userColor, cpuColor)

	return cpuColor

def main():
	board = setupBoard()

	print("Welcome to Reversi! Let's get started.")

	cpuColor = selectColor()

	printBoard(board)


main()