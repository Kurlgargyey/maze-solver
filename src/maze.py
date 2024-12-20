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
		self.rng = random.seed(seed)

		self._create_cells()
		self._break_entrance_and_exit()

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

	def _draw_cell(self, i, j):
		if self._win is not None:
			self._cells[i][j].draw()
			self._animate()

	def _animate(self):
		self._win.redraw()
		time.sleep(0.001)