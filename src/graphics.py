from tkinter import Tk, BOTH, Canvas


class Window:
	def __init__(self, width, height):
		self.__root = Tk()
		self.__root.title("Maze Solver")
		self.__root.protocol("WM_DELETE_WINDOW", self.close)
		self.__canvas = Canvas(self.__root, {"bg":"white", "height":f"{height}", "width":f"{width}"})
		self.__canvas.pack(fill=BOTH, expand=1)
		self.__running = False

	def redraw(self):
		self.__root.update_idletasks()
		self.__root.update()

	def wait_for_close(self):
		self.__running = True
		while self.__running:
			self.redraw()
		print("window closed...")

	def close(self):
		self.__running = False

	def draw_line(self, line, fill_color):
		line.draw(self.__canvas, fill_color)

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y


class Line:
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2

	def draw(self, canvas, fill_color):
		canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill = fill_color, width = 2)

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
		if self.has_left_wall:
			self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "black")
		if self.has_right_wall:
			self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "black")
		if self.has_top_wall:
			self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "black")
		if self.has_bottom_wall:
			self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "black")

	def center(self):
		return Point(self._x1+(self._x2-self._x1)/2,self._y1+(self._y2-self._y1)/2)

	def draw_move(self, to_cell, undo=False):
		fill_color = "gray" if undo else "red"
		self_center = self.center()
		to_center =	to_cell.center()
		self._win.draw_line(Line(self_center, to_center), fill_color)