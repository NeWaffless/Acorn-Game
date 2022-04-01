import sys
from game import Game
from game_parser import read_lines, parse
from cells import (
	Start,
	Teleport
)

def solve(mode, board):
	pos_list = []
	start_pos = Start.step(parse(read_lines(board)))
	pos_list.append(start_pos)
	paths = [""]
	game_solved = False
	possible_moves = ["s", "d", "w", "a", "e"]
	# debug_count = 0

	past_positions = [[start_pos]]
	num_buckets = [0]
	change_to_air = [[]]

	while game_solved == False:
		if mode == "DFS":
			pos_list_index = len(pos_list) - 1
			paths_index = len(paths) - 1
			past_pos_index = len(past_positions) - 1
			num_buckets_index = len(num_buckets) - 1
			air_index = len(change_to_air) - 1
		elif mode == "BFS":
			pos_list_index = 0
			paths_index = 0
			past_pos_index = 0
			num_buckets_index = 0
			air_index = 0

		try:
			curr_pos = pos_list.pop(pos_list_index)
		except:
			return False
		curr_path = paths.pop(paths_index)
		curr_past_pos = past_positions.pop(past_pos_index)
		curr_bucket = num_buckets.pop(num_buckets_index)
		curr_air_spaces = change_to_air.pop(air_index)

		run_e = False

		for direction in possible_moves:
			past_pos_copy = curr_past_pos
			air_copy = curr_air_spaces.copy()

			temp_game = Game(board, curr_pos, curr_bucket, air_copy, True)
			if direction == "e":
				if isinstance(temp_game.current, Teleport) and curr_path[len(curr_path) - 1] != "e":
					run_e = True
			temp_game.solve_move(direction, past_pos_copy)

			if direction == "e" and run_e == False:
				pass
			elif temp_game.move_solve_pos == True and temp_game.prev_pos == False:
				paths.append(curr_path + direction)
				if temp_game.solved == True:
					game_solved = True
					break

				pos_list.append([temp_game.player.row, temp_game.player.col])

				if temp_game.player.num_water_buckets > curr_bucket:
					past_pos_copy = []
					air_copy.append([temp_game.player.row, temp_game.player.col])
				if temp_game.player.num_water_buckets < curr_bucket:
					air_copy.append([temp_game.player.row, temp_game.player.col])
				if temp_game.solve_tele_check == False:
					past_pos_copy.append([temp_game.player.row, temp_game.player.col])

				past_positions.append(past_pos_copy)
				change_to_air.append(air_copy)
				num_buckets.append(temp_game.player.num_water_buckets)
				# debug_count += 1
		# print(debug_count)
	return paths[len(paths) - 1]



if __name__ == "__main__":
	board = sys.argv[1]
	solution_found = False
	if len(sys.argv) < 2:
		print("Usage: python3 solver.py <filename><mode>")
		sys.exit()
	mode = sys.argv[2]
	solution = solve(mode, board)

	if solution != False:
		solution_found = True

	if solution_found:
		num_moves = len(solution)
		path_output = 'Path:'
		temp_int = 0

		while temp_int < len(solution):
			path_output += ' {},'.format(solution[temp_int])
			temp_int += 1

		print("Path has {} moves.".format(num_moves))
		print(path_output[:-1])
	else:
		print("There is no possible path.")