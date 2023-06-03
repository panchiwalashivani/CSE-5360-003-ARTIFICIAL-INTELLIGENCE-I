#NAME: Shivani Panchiwala
#UTA ID: 1001982478

import sys
from MaxConnect4Game import *
from AlphaBetaDecision import *

def oneMoveGame(currentGame):
    if currentGame.pieceCount == 42:    # Is the board full already?
        print('BOARD FULL\n\nGame Over!\n')
        sys.exit(0)

    # currentGame.aiPlay() # Make a move (only random is implemented)
    selectedColumn, selectedValue = AlphaBetaDecision(currentGame)
    currentGame.playPiece(selectedColumn)
    print('\n\nmove %d: Player %d, column %d\n' % (currentGame.checkPieceCount(), currentGame.currentTurn, selectedColumn+1))

    print('Game state after move:')
    currentGame.printGameBoard()

    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    currentGame.printGameBoardToFile()
    currentGame.gameFile.close()


def interactiveGame(currentGame, first_Player):
    # Fill me in
    currentGame.currentTurn = 1
    if first_Player == 'human-first':
        currentGame.currentTurn = 2
    while not currentGame.checkPieceCount() == 42:
        if currentGame.currentTurn == 1:
            currentGame.currentTurn = 2
            selectedColumn, selectedValue = AlphaBetaDecision(currentGame)
            currentGame.currentTurn = 1
            currentGame.playPiece(selectedColumn)
            print('\n\nmove %d: Player %d, column %d\n' % (currentGame.checkPieceCount(), currentGame.currentTurn, selectedColumn + 1))
            currentGame.currentTurn = 2

            try:
                currentGame.gameFile = open('c.txt', 'w')
            except:
                pass
        else:
            isValidMove = 0
            while not isValidMove:
                humanColumn = raw_input('\nPlease enter empty column number to play from 1 to 7: ')
                while int(humanColumn) not in range(1,8):
                    humanColumn = raw_input('\nPlease enter empty column number to play from 1 to 7: ')
                
                isValidMove = currentGame.playPiece(int(humanColumn) - 1)
            currentGame.currentTurn = 1
            
            try:
                currentGame.gameFile = open('human.txt', 'w')
            except:
                pass
        
        currentGame.printGameBoardToFile()
        currentGame.gameFile.close()
        print('Game state after move:')
        currentGame.printGameBoard()
        currentGame.countScore()
        print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
    
    print('BOARD FULL\n\nGame Over!\n')
    sys.exit(0)
    # sys.exit('Interactive mode is currently not implemented')


def main(argv):
    # Make sure we have enough command-line arguments
    if len(argv) != 5:
        print('Four command-line arguments are needed:')
        print('Usage: %s interactive [input_file] [computer-first/human-first] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)

    game_mode, inFile = argv[1:3]

    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)

    currentGame = maxConnect4Game() # Create a game

    currentGame.depthLimt = int(argv[4])

    if game_mode == 'one-move':
        # Try to open the input file
        try:
            currentGame.gameFile = open(inFile, 'r')
        except IOError:
            sys.exit("\nError opening input file.\nCheck file name.\n")

        # Read the initial game state from the file and save in a 2D list
        file_lines = currentGame.gameFile.readlines()
        currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
        currentGame.currentTurn = int(file_lines[-1][0])
        currentGame.gameFile.close()
    else:
        isFileFound = 1
        # Try to open the input file
        try:
            currentGame.gameFile = open(inFile, 'r')
        except IOError:
            isFileFound = 0

        if isFileFound:
            # Read the initial game state from the file and save in a 2D list
            file_lines = currentGame.gameFile.readlines()
            currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
            currentGame.currentTurn = int(file_lines[-1][0])
            currentGame.gameFile.close()

    print('\nMaxConnect-4 game\n')
    print('Game state before move:')
    currentGame.printGameBoard()

    # Update a few game variables based on initial state and print the score
    currentGame.checkPieceCount()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    if game_mode == 'interactive':
        first_Player = argv[3]
        if not first_Player == 'computer-first' and not first_Player == 'human-first':
            print('%s is an unrecognized player name' % first_Player)
            sys.exit(2)
        
        interactiveGame(currentGame, first_Player) # Be sure to pass whatever else you need from the command line
    else: # game_mode == 'one-move'
        # Set up the output file
        outFile = argv[3]
        try:
            currentGame.gameFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(currentGame) # Be sure to pass any other arguments from the command line you might need.


if __name__ == '__main__':
    main(sys.argv)
