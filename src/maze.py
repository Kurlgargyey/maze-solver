from cell import Cell
import time
import random

class Maze:
	def __init__(
			self,
			x1,
			y1,
			num_rows,
			num_cols,
			cell_size_x,
			cell_size_y,
			win = None,
			seed = None
		):
		self._x1 = x1
		self._y1 = y1
		self._num_rows = num_rows
		self._num_cols = num_cols
		self._cell_size_x = cell_size_x
		self._cell_size_y = cell_size_y

		self._win = win
		if seed:
			random.seed(seed)

		self._create_cells()
		self._break_entrance_and_exit()
		self._break_walls_r(0, 0)

	def _create_cells(self):
		self._cells = [[Cell(window=self._win) for i in range(self._num_rows)] for j in range(self._num_cols)]

		for i, col in enumerate(self._cells):
			for j, cell in enumerate(col):
				cell = self._cells[i][j]
				x = self._x1+self._cell_size_x*i
				y = self._y1+self._cell_size_y*j
				cell._x1 = x
				cell._x2 = x+self._cell_size_x
				cell._y1 = y
				cell._y2 = y+self._cell_size_y
				self._draw_cell(i, j)

	def _break_entrance_and_exit(self):
		self._cells[0][0].has_top_wall = False
		self._draw_cell(0,0)
		self._cells[-1][-1].has_bottom_wall = False
		self._draw_cell(-1, -1)

	def _break_walls_r(self, i, j):
		self._cells[j][i].visited = True
		while True:
			queue = []
			if j > 0 and not self._cells[j-1][i].visited:
				queue.append((i, j-1))
			if i > 0 and not self._cells[j][i-1].visited:
				queue.append((i-1, j))
			if j < self._num_cols-1 and not self._cells[j+1][i].visited:
				queue.append((i, j+1))
			if i < self._num_rows-1 and not self._cells[j][i+1].visited:
				queue.append((i+1, j))
			if len(queue) == 0:
				self._draw_cell(i, j)
				return
			next_i, next_j = random.choice(queue)
			self._break_wall(i, j, next_i, next_j)
			self._break_walls_r(next_i, next_j)

	def _break_wall(self, i1, j1, i2, j2):
		cell1 = self._cells[j1][i1]
		cell2 = self._cells[j2][i2]

		if j1 == j2:
			if i2 < i1:
				cell1.has_top_wall = False
				cell2.has_bottom_wall = False
			else:
				cell1.has_bottom_wall = False
				cell2.has_top_wall = False
		else:
			if j2 < j1:
				cell1.has_left_wall = False
				cell2.has_right_wall = False
			else:
				cell1.has_right_wall = False
				cell2.has_left_wall = False

		self._draw_cell(i1, j1)
		self._draw_cell(i2, j2)

	def _reset_cells_visited(self):
		for row in self._cells:
			for cell in row:
				cell.visited = False

	def _draw_cell(self, i, j):
		if self._win is not None:
			self._cells[j][i].draw()
			self._animate()

	def _animate(self):
		self._win.redraw()
		time.sleep(0.001)