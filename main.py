# Lund University | EDAF70 | Project 1 - Reversi
# Rachit Agarwal | Jay Mangrulkar

import numpy as np
import string
import re

# Introduces the game and some basic info
def gameWelcome():
	print("Welcome to Reversi!")
	print("To learn how to play, please visit https://www.mathsisfun.com/games/reversi.html.")
	print("When it's your move, enter a row letter and column number adjacently, ex. \'c5\'.")
	print("You can also enter \'quit\' to quit, or \'help\' if you need a move suggestion.")
	print("Enjoy, and good luck!")

# Creates empty game board
def createEmptyBoard():
	board = []
	size = 8
	for row in range(0,size):
		board.append([])
		for col in range(0,size):
			# ' ' = empty, O = white, X = black
			# O is letter O not 0
			board[row].append(" ")
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
	print("Current Board:\n")
	print("  | a | b | c | d | e | f | g | h |")
	print("  " + "".join(["-" for i in range(33)]))
	for row in range(0,8):
		rowVals = " | ".join(board[row])
		print (str(row + 1) + " | " + rowVals + " |")
		print("  " + "".join(["-" for i in range(33)]))
	# print(np.matrix(board))

# Handles user color selection
def selectColor():
	userColorInput = raw_input("What color would you like to play as? Please enter \'black\' or \'white\'. ")
	
	if userColorInput == "white" or userColorInput == "w":
		userColor = "white"
		cpuColor = "black"
	else:
		userColor = "black"
		cpuColor = "white"

	print("Great! You are playing as %s. The CPU is playing as %s." % (userColor, cpuColor))

	return userColor, cpuColor

# Returns whether or not a given move for a player is valid
def isValidMove(board, moveColor, row, col):
	return True

# Returns a list of all valid moves given the board and turn/move color
def getAllValidMoves(board, moveColor):
	allValidMoves = []

	for row in range(0,8):
		for col in range(0,8):
			if (isValidMove(board, moveColor, row, col)):
				allValidMoves.append((row, col))

	return allValidMoves

def main():
	board = setupBoard()
	gameWelcome()

	userColor, cpuColor = selectColor()
	moveColor = "black"

	rowLetterToNum = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7 }
	rowNumToLetter = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}

	while True:
		printBoard(board)
		validMoves = getAllValidMoves(board, moveColor)

		if len(validMoves) == 0:
			print ("There are no valid moves for " + moveColor + ". Passing turn.")

		if (userColor == moveColor):
			userCanMove = True
			while userCanMove:
				userMove = raw_input("Your move! ")
				if (userMove == "quit"):
					sys.exit()
				if (userMove == "help"):
					print("TODO")
					#f
				if len(re.findall(r'[a-h][1-8]', userMove)) != 1:
					print("Looks like you didn't format your move correctly. Example: c6")
					continue


				break

		break

main()