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
			# 0 = empty, 1 = white, 2 = black
			board[row].append(0)
	return board

# Prints the game board
def printBoard(board):
	print np.matrix(board)

def main():
	board = createEmptyBoard()
	printBoard(board)

main()