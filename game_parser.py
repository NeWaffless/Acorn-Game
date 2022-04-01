from sys import exit
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)

cell_dict = {
	" ": Air(),
	"X": Start(),
    "Y": End(),
    "*": Wall(),
    "F": Fire(),
    "W": Water()
}

def read_lines(filename):
    """Read in a file and return the contents as a list of strings."""

    lines = []
    board_file = open(filename,'r')

    i = 0
    while True:
    	curr_line = board_file.readline()
    	if curr_line == "":
    		break
    	lines.append(curr_line)
    	i += 1
    
    board_file.close()

    
    return lines

def parse(lines):
    """Transform the input into a grid.

    Arguments:
        lines -- list of strings representing the grid

    Returns:
        list -- contains list of lists of Cells
    """

    #grid, list of cells
    board = []
    start_fin_cnt = [0, 0]

    #teleport number, teleport row, teleport col
    tn = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    tr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    tc = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for row in range(len(lines)):
    	board.append([])
    	for col in range(len(lines[row])):
            #if not new line, and cell exists
    		if lines[row][col] != "\n" and lines[row][col] in cell_dict:
    			board[row].append(cell_dict.get(lines[row][col]))
    			if lines[row][col] == "X":
    				start_fin_cnt[0] += 1
    			elif lines[row][col] == "Y":
    				start_fin_cnt[1] += 1
    		elif lines[row][col] != "\n":
                #check if non-dict char is number, therefore teleporter
    			try:
    				int(lines[row][col])
    			except:
    				raise ValueError("Bad letter in configuration file: {}.".format(lines[row][col]))

    			board[row].append(Teleport(lines[row][col], row, col))

                #rbt = readability
    			rbt = int(lines[row][col])
    			if rbt == 0:
    				raise ValueError("Bad letter in configuration file: 0.")
    			tn[rbt] += 1
                #if one teleport, assign position to row and col
                #if two teleport, pair with position in row and col
    			if tn[rbt] == 1:
    				tr[rbt] = row
    				tc[rbt] = col
    			elif tn[rbt] == 2:
    				board[row][col].pair(board[tr[rbt]][tc[rbt]])
    				board[tr[rbt]][tc[rbt]].pair(board[row][col])

    if start_fin_cnt[0] <= 0 or start_fin_cnt[0] >= 2:
    	raise ValueError("Expected 1 starting position, got {}.".format(start_fin_cnt[0]))
    if start_fin_cnt[1] <= 0 or start_fin_cnt[1] >= 2:
    	raise ValueError("Expected 1 ending position, got {}.".format(start_fin_cnt[1]))
    for pad in range(len(tn)):
    	if tn[pad] != 0 and tn[pad] != 2:
    		raise ValueError("Teleport pad {} does not have an exclusively matching pad.".format(pad))
    	pad += 1

    return board