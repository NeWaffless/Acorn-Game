from player import Player

def grid_to_string(grid, player):
    """Turns a grid and player into a string

    Arguments:
        grid -- list of list of Cells
        player -- a Player with water buckets

    Returns:
        string: A string representation of the grid and player.
    """

    if type(grid) != list:
    	raise TypeError("Grid is not list of lists.")
    if len(grid) <= 0:
    	raise IndexError("Grid is empty.")
    for col in grid:
    	if len(col) <= 0:
    		raise IndexError("Column is empty.")
    if type(player) != Player:
    	raise TypeError("Player is not type player.")
    
    board_string = ""
    bucket_s = "s"

    for i in range(len(grid)):
    	for j in range(len(grid[i])):
    		#placing player
    		if player.row == i and player.col == j:
    			board_string += player.display
    		else:
    			board_string += str(grid[i][j].display)
    	board_string += "\n"

    if player.num_water_buckets == 1:
    	bucket_s = ""
    else:
    	bucket_s = "s"

    board_string += "\nYou have {} water bucket{}.\n".format(player.num_water_buckets, bucket_s)
    return board_string