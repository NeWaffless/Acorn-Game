from game_parser import read_lines, parse
from grid import grid_to_string
from player import Player
from cells import (
	Start,
	End,
	Air,
	Wall,
	Fire,
	Water,
	Teleport
)

class Game:
	def __init__(self, filename, start_pos, buckets, no_water, solving):
		self.state = True
		self.board_var = parse(read_lines(filename))

		#interacted water & fire cells in solver change to air
		if solving == True and (no_water != False and len(no_water) > 0):
			for space in no_water:
				if len(space) > 0:
					self.board_var[space[0]][space[1]] = Air()

		self.player = Player(self.board_var, start_pos[0], start_pos[1], buckets)
		self.board = grid_to_string(self.board_var, self.player)
		self.alt_text = False
		self.alt_message = ""
		self.num_moves = 0
		self.move_list = ""
		self.result = ""

		#solver variables
		if solving != True and solving != False:
			solving = False
		self.solving = solving
		self.move_solve_pos = True
		self.solved = False
		self.prev_pos = False
		self.solve_tele_check = False
		self.current = self.board_var[self.player.row][self.player.col]

	def game_move(self, move_input):
		self.player.move(self, self.board_var, move_input, False)
		self.board = grid_to_string(self.board_var, self.player)

		if self.alt_text == True:
			self.board += "\n{}\n".format(self.alt_message)
			self.alt_text = False

		if self.state != True:
			self.num_moves += 1
			self.move_list += " {},".format(move_input)
			self.move_list = self.move_list.lower()
			return False
		#don't print if wall
		elif self.player.wall == True:
			return self.board
		else:
			self.num_moves += 1
			self.move_list += " {},".format(move_input)
			return self.board

	def solve_move(self, move_input, past_pos):
		self.player.move(self, self.board_var, move_input, past_pos)