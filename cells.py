class Start:
	def __init__(self):
		self.display = 'X'

	def step(grid):
		start_pos = []

		for i in range(len(grid)):
			for j in range(len(grid[i])):
				if grid[i][j].display == 'X':
					start_pos.append(i)
					start_pos.append(j)

		return start_pos


class End:
	def __init__(self):
		self.display = 'Y'

	def step(game):
		game.result = "====== YOU WIN! ====="
		game.state = False
		game.solved = True


class Air:
	def __init__(self):
		self.display = ' '

	def step(self):
		pass


class Wall:
	def __init__(self):
		self.display = '*'

	def step(player, game, grid, axis, direction):
		if axis == "row":
			#rbt = readability
			rbt = player.row + direction
			if (rbt < 0 or rbt >= len(grid)) or isinstance(grid[rbt][player.col], Wall):
				game.alt_text = True
				game.alt_message = "You walked into a wall. Oof!"
				game.move_solve_pos = False
				player.wall = True
				return True
			else:
				return False

		if axis == "col":
			rbt = player.col + direction
			if (rbt < 0 or rbt >= len(grid[0])) or isinstance(grid[player.row][rbt], Wall):
				game.alt_text = True
				game.alt_message = "You walked into a wall. Oof!"
				game.move_solve_pos = False
				player.wall = True
				return True
			else:
				return False

class Water:
	def __init__(self):
		self.display = 'W'

	def step(player, grid, game):
		player.num_water_buckets += 1
		grid[player.row][player.col] = Air()
		game.alt_text = True
		game.alt_message = "Thank the Honourable Furious Forest, you've found a bucket of water!"


class Fire:
	def __init__(self):
		self.display = 'F'

	def step(player, grid, game):
		if player.num_water_buckets > 0:
			player.num_water_buckets -= 1
			#incase water buckets < 0
			if player.num_water_buckets < 0:
				player.num_water_buckets = 0
			#change tile to air
			grid[player.row][player.col] = Air()
			game.alt_text = True
			game.alt_message = "With your strong acorn arms, you throw a water bucket at the fire. You acorn roll your way through the extinguished flames!"
		elif game.solving == True and player.num_water_buckets <= 0:
			game.move_solve_pos = False
		else:
			game.result = "===== GAME OVER ====="
			game.state = False


class Teleport:
	def __init__(self, tele_num, row, col):
		self.display = str(tele_num)  # You'll need to change this!
		self.pair
		self.row = row
		self.col = col

	def step(self, player, grid, game):
		player.row = self.pair.row
		player.col = self.pair.col

		game.solve_tele_check = True
		game.alt_text = True
		game.alt_message = "Whoosh! The magical gates break Physics as we know it and opens a wormhole through space and time."

	def pair(self, tele2):
		#pairs teleporters of same number
		self.pair = tele2