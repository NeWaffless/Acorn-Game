# Acorn-Game
This acorn game is a simple command line text game programmed in python for a university assessment. The game takes in user input in the form of entered key inputs, and outputs the board state. The game requires python to run, and is played entirely within the command line.

## Running the game
1. Download the code and extract onto your local machine.
2. Navigate to the local folder within the command line of your choice.
3. Enter the following command into your command line ```console python run.py boards/[ENTER BOARD HERE]```
To play the game, use the 'wasd' keys to move, 'e' to wait, and 'q' to quit. Make sure to press enter after each key command for the game to register that input.

## Boards
There are some game boards within the 'boards' folder. More can be created as you like using the following symbols:
- X = start (exactly 1 required)
- Y = finish (exactly 1 required)
- * = wall
- ' ' = empty space
- W = water
- F = fire
- Numbers 0 - 9 = teleports (must come in pairs)

## Solver
There is a ```python solver.py``` script that can perform a breadth-first search and depth-first search on an inputted board, which outputs a sequence of inputs that can be used to solve that board (provided one exists). Using the solver's bfs search results in a given boards fastest solution.
To use the solver, enter one of the following command into your command line for the respective search type:
BFS - ```console python solver.py boards/[ENTER BOARD HERE] bfs```
DFS - ```console python solver.py boards/[ENTER BOARD HERE] dfs```

## Contributors
Aidan Walbran - Programmer
