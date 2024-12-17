from cell import Cell
import time

class Maze:
	def __init__(
			self,
			x1,
			y1,
			num_rows,
			num_cols,
			cell_size_x,
			cell_size_y,
			win = None
		):
		self._x1 = x1
		self._y1 = y1
		self._num_rows = num_rows
		self._num_cols = num_cols
		self._cell_size_x = cell_size_x
		self._cell_size_y = cell_size_y
		self._win = win
		self._create_cells()

	def _create_cells(self):
		self._cells = [[Cell(window=self._win) for i in range(self._num_rows)] for j in range(self._num_cols)]

		for i, col in enumerate(self._cells):
			for j, cell in enumerate(col):
				self._draw_cell(i, j)

	def _draw_cell(self, i, j):
		cell = self._cells[i][j]
		x = self._x1+self._cell_size_x*i
		y = self._y1+self._cell_size_y*j
		cell._x1 = x
		cell._x2 = x+self._cell_size_x
		cell._y1 = y
		cell._y2 = y+self._cell_size_y
		if self._win is not None:
			cell.draw()
			self._animate()

	def _animate(self):
		self._win.redraw()
		time.sleep(0.2)