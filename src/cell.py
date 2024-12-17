from graphics import Line, Point

class Cell:
	def __init__(self,
			  p1,
			  p2,
			  window,
			  has_left_wall=True,
			  has_right_wall=True,
			  has_top_wall=True,
			  has_bottom_wall=True,
			  ):
		self.has_left_wall = has_left_wall
		self.has_right_wall = has_right_wall
		self.has_top_wall = has_top_wall
		self.has_bottom_wall = has_bottom_wall
		self._x1 = p1.x
		self._x2 = p2.x
		self._y1 = p1.y
		self._y2 = p2.y
		self._win = window

	def draw(self):
		if self._win is None:
			return
		if self.has_left_wall:
			self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)))
		if self.has_right_wall:
			self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)))
		if self.has_top_wall:
			self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)))
		if self.has_bottom_wall:
			self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)))

	def center(self):
		return Point(self._x1+(self._x2-self._x1)/2,self._y1+(self._y2-self._y1)/2)

	def draw_move(self, to_cell, undo=False):
		fill_color = "gray" if undo else "red"
		self_center = self.center()
		to_center =	to_cell.center()
		self._win.draw_line(Line(self_center, to_center), fill_color)