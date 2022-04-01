from game import Game
import os
import sys
from game_parser import read_lines, parse
from cells import Start

try:
	test_board = read_lines(sys.argv[1])
except:
	print("{} does not exist!".format(sys.argv[1]))
	sys.exit()

init_game_board = parse(test_board)
start_pos = Start.step(init_game_board)
curr_game = Game(sys.argv[1], start_pos, 0, False, False)
# os.system("clear")
print(curr_game.board)
move_list = "wasdeqWASDEQ"

while True:
	curr_move = str(input("Input a move: "))

	if len(curr_move) == 1 and curr_move in move_list:
		# os.system("clear")
		if curr_move == "q":
			print("\nBye!")
			sys.exit()
		game_state = curr_game.game_move(curr_move)
		if game_state == False:
			break
		print(game_state)
	else:
		# os.system("clear")
		print(curr_game.board)
		print("Please enter a valid move (w, a, s, d, e, q).\n")

print(curr_game.board)

if curr_game.result == "===== GAME OVER =====":
	print("\nYou step into the fires and watch your dreams disappear :(.\n" +
		  "\nThe Fire Nation triumphs! The Honourable Furious Forest is reduced" +
		  " to a pile of ash and is scattered to the winds by the next storm... " +
		  "You have been roasted.\n")
elif curr_game.result == "====== YOU WIN! =====":
	print("\nYou conquer the treacherous maze set up by the Fire Nation and reclaim " +
		  "the Honourable Furious Forest Throne, restoring your hometown back to its " +
		  "former glory of rainbow and sunshine! Peace reigns over the lands.\n")
else:
	print("Something went wrong here?!")

move_plural = 's'

if curr_game.num_moves == 1:
	move_plural = ''

print("You made {} move{}.\nYour move{}:{}\n".format \
	  (curr_game.num_moves, move_plural, move_plural, curr_game.move_list[:-1]))
print("=====================\n{}\n=====================".format(curr_game.result), end="")