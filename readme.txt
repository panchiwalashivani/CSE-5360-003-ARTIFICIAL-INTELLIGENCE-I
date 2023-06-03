NAME: Shivani Panchiwala
UTA ID: 1001982478


I used Python as my programming language for Task2

Code Structure:
1) "maxconnect4.py" - it is the main file for running the program
2) "MaxConnect4Game.py" - It contains the game structure
3) "AlphaBetaDecision.py" - It is implements the alpha-beta algorithm
4) "ExecutionTime.xlsx" - It contains the table of depth limit vs runtime


Eval function is named as "score_Eval" in "MaxConnect4Game.py" file.
It check whose score is greater, player1 or player2 (human player).
If player1's score is greater then player2's then it will return positive value of player1's score.
If player1's score is less then player2's then it will return negative value of player2's score.
If both values are then it will return 0


Few changes are made in "MaxConnect4Game.py":
1) Added a function for eval
2) Return "checkPieceCount" 
3) Added depth limit variable in init function

Changes are made in "maxconnect4.py":
1) Changed a bit in main function to read depth limit
2) Modified one-move function
3) Added logic in interactive function

Added new file "AlphaBetaDecision.py" it contains 4 functions:
1) "AlphaBetaDecision" - It is main function to start alpha-beta
2) "Max_Value" - Finds maximum value from it's immediate children
3) "Min_Value" - Finds minimum value from it's immediate chlidren
4) "Successor" - It finds the immediate successors of a given state

How to run the code?

Run program using exactly following format for one-move game format:
"python maxconnect4.py one-move input1.txt output1.txt 4"

In above line "input1.txt" is the input file, it can be any name, "output1.txt" is the output file, it can be any name and "4" is the depth limit.

Run program using exactly following format for interactive game format:
"python maxconnect4.py interactive input1.txt computer-first 4"

In above line "input1.txt" is the input file, it can be any name, "computer-first" is the flag that who plays first, it can also be "human-first" and "4" is the depth limit.
