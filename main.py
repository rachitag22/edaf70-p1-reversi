# Lund University | EDAF70 | Project 1 - Reversi
# Rachit Agarwal | Jay Mangrulkar

import numpy as np
import string
import re


colLetterToNum = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7 }
colNumToLetter = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}
colorToLetter = {"white": "O", "black": "X"}

# Introduces the game and some basic info
def gameWelcome():
	print("Welcome to Reversi!")
	print("To learn how to play, please visit https://www.mathsisfun.com/games/reversi.html.")
	print("When it's your move, enter a row letter and column number adjacently, ex. \'c5\'.")
	print("You can also enter \'quit\' to quit, or \'help\' if you need a move suggestion.")
	print("Remember that O is white, X is black. You will be able to choose your color in a second.")
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

	board[3][3] = "X"
	board[4][4] = "X"
	board[3][4] = "O"
	board[4][3] = "O"

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

# Converts a board letter/piece (O or X) to either -1 or 1
def convertColor(val):
	if (val == "X" or val == "black"):
		return 1
	elif (val == "O" or val == "white"):
		return -1
	else:
		return 0

def convertTileTupleToString(tile):
	# print("TILE: " + str(tile[1]) + " " + str(tile[0]))
	return colNumToLetter[tile[1]] + str(tile[0]+1)

def getFlippedTilesList(board, moveColor, row, col):
	tilesToFlip = []

	moveConst = convertColor(moveColor)
	otherConst = moveConst * -1

	for deltaRow in range(-1,2):
		for deltaCol in range(-1,2):
			# print("Testing next tile, dX and dY: " + str(deltaRow) + ", " + str(deltaCol))
			foundOtherColor = False
			nextTile = otherConst
			continueSearch = True

			nextTileRow = row + deltaRow
			nextTileCol = col + deltaCol

			tempTilesToFlip = []

			while nextTile == otherConst and continueSearch == True:

				try:
					if (nextTileRow < 0 or nextTileRow > 7 or nextTileCol < 0 or nextTileCol > 7):
						continueSearch = False
						break

					nextTile = convertColor(board[nextTileRow][nextTileCol])
					# print ("Next Tile @ " + str(nextTileRow) + ", " + str(nextTileCol))

					if nextTile == 0:
						continueSearch = False
					elif nextTile == otherConst:
						# print("Next tile: " + str(nextTileRow) + "-" + str(nextTileCol) + ": " + str(nextTile))
						tempTilesToFlip.append((nextTileRow, nextTileCol))
						foundOtherColor = True
						continueSearch = True

					# We've traversed and found the move's color, AND have seen other chips along the way ("end of the line")
					elif foundOtherColor == True:
						print("found other color")
						tilesToFlip.extend(tempTilesToFlip)
						continue

					nextTileRow += deltaRow
					nextTileCol += deltaCol

				except:
					continueSearch = False

	return tilesToFlip
	

# Flips tiles and returns resultant board upon making a move (which should already be validated)
def flipTilesAndReturnNewBoard(board, moveColor, row, col):
	for (flipRow, flipCol) in tilesToFlip:
		board[flipRow][flipCol] = "X" if board[flipRow][flipCol] == "O" else "O"

	tilesFlippedWithLetters = []
	for tile in tilesToFlip:
		tilesFlippedWithLetters.append(convertTileTupleToString(tile))

	print("Tiles Flipped: " + str(tilesFlippedWithLetters))
	return board


# Returns whether or not a given move for a player is valid
def isValidMove(board, moveColor, row, col):
	if (flipTilesAndReturnNewBoard)

def isValidMoveOld(board, moveColor, row, col):
	valid = False

	moveConst = convertColor(moveColor)
	otherConst = moveConst * -1

	if board[row][col] != " ":
		return False

	for deltaRow in range(-1,2):
		for deltaCol in range(-1,2):
			foundOtherColor = False
			nextTile = otherConst
			continueSearch = True

			nextTileRow = row + deltaRow
			nextTileCol = col + deltaCol

			while nextTile == otherConst and continueSearch == True:

				try:
					nextTile = convertColor(board[nextTileRow][nextTileCol])

					if nextTile == 0:
						continueSearch = False
					elif nextTile == otherConst:
						foundOtherColor = True
						continueSearch = True
					elif foundOtherColor == True:
						return True

					nextTileRow += deltaRow
					nextTileCol += deltaCol

				except:
					continueSearch = False

	return False

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

	while True:
		printBoard(board)
		validMoves = getAllValidMoves(board, moveColor)

		if len(validMoves) == 0:
			print ("There are no valid moves for " + moveColor + ". Passing turn.")
			userNeedsToMove = False
			moveColor = "white" if (userColor == "black") else "black"
		else:
			userNeedsToMove = True

		validMovesWithLetters = []
		for move in validMoves:
			validMovesWithLetters.append(convertTileTupleToString(move))

		print("Valid moves for " + moveColor + ": " + str(validMovesWithLetters))

		# User's turn/move
		if (userColor == moveColor):
			while userColor == moveColor:
				userMove = raw_input("Your move! Remember, your color is " + str(userColor) + " (" + str(colorToLetter[userColor]) + ") ")
				if (userMove == "quit"):
					sys.exit()
				if (userMove == "help"):
					
					print("Here's a list of valid moves: " + str(validMovesWithLetters))
					print("Go ahead, you got this.")
					continue
				if len(re.findall(r'[a-h][1-8]', userMove)) != 1:
					print("Looks like you didn't format your move correctly. Example: c6")
					continue
				colLetter = re.search(r'([a-h])([1-8])', userMove).group(1)
				colIndex = colLetterToNum[colLetter]
				rowIndex = int(re.search(r'([a-h])([1-8])', userMove).group(2)) - 1

				# print(isValidMove(board, userColor, rowIndex, colIndex))

				if (rowIndex, colIndex) not in validMoves:
					print("That's not a valid move. Please try again.")
					print()
					continue

				print("Nice move! " + moveColor + " placing tile on " + userMove)
				board[rowIndex][colIndex] = "X" if userColor == "black" else "O"
				
				board = flipTilesAndReturnNewBoard(board, moveColor, rowIndex, colIndex)

				moveColor = cpuColor

		# Computer's turn/move
		else:
			# Implement algorithm here
			cpuMove = validMoves[0]
			(rowIndex, colIndex) = cpuMove

			print("CPU move! " + moveColor + " placing tile on " + convertTileTupleToString(cpuMove))
			board[rowIndex][colIndex] = "X" if cpuColor == "black" else "O"
			board = flipTilesAndReturnNewBoard(board, moveColor, rowIndex, colIndex)

			moveColor = userColor

main()