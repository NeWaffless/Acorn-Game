from cells import (
	Start,
	End,
	Air,
	Wall,
	Fire,
	Water,
	Teleport
)

class Player:
	def __init__(self, grid, row, col, buckets):
		self.display = 'A'
		self.num_water_buckets = buckets
		#default position values
		self.row = 0
		self.col = 0
		if row >= 0 and row < len(grid):
			self.row = row
		if col >= 0 and col < len(grid[0]):
			self.col = col
		self.move_state = False
		self.wall = False

	def check_step(self, grid, game):
		if isinstance(grid[self.row][self.col], Water):
			Water.step(self, grid, game)
		elif isinstance(grid[self.row][self.col], Fire):
			Fire.step(self, grid, game)
		elif isinstance(grid[self.row][self.col], Teleport):
			Teleport.step(grid[self.row][self.col], self, grid, game)
		elif isinstance(grid[self.row][self.col], End):
			End.step(game)

	def move(self, game, grid, move_input, past_pos):
		self.wall = False

		#check past positions while solving
		if past_pos != False:
			for i in range(len(past_pos)):
				if move_input == "w" and [self.row - 1, self.col] in past_pos:
					game.prev_pos = True
				if move_input == "s" and [self.row + 1, self.col] in past_pos:
					game.prev_pos = True
				if move_input == "a" and [self.row, self.col - 1] in past_pos:
					game.prev_pos = True
				if move_input == "d" and [self.row, self.col + 1] in past_pos:
					game.prev_pos = True

		if move_input == "w" or move_input == "W":
			if Wall.step(self, game, grid, "row", -1) == False:
				self.row -= 1
				game.move_solve_pos = True
				self.check_step(grid, game)
		if move_input == "s" or move_input == "S":
			if Wall.step(self, game, grid, "row", 1) == False:
				self.row += 1
				game.move_solve_pos = True
				self.check_step(grid, game)
		if move_input == "a" or move_input == "A":
			if Wall.step(self, game, grid, "col", -1) == False:
				self.col -= 1
				game.move_solve_pos = True
				self.check_step(grid, game)
		if move_input == "d" or move_input == "D":
			if Wall.step(self, game, grid, "col", 1) == False:
				self.col += 1
				game.move_solve_pos = True
				self.check_step(grid, game)
		if move_input == "e" or move_input == "E":
			self.check_step(grid, game)