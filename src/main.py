from graphics import Window, Point, Line, Cell

def main():
	win = Window(800, 600)
	p1 = Point(100, 200)
	p2 = Point(200, 350)
	line = Line(p1, p2)
	p3 = Point(700, 400)
	cell = Cell(p1, p3, win)
	cell2 = Cell(Point(250, 250), Point(500, 500), win, has_bottom_wall=False)
	cell2.draw()
	cell.draw()
	cell.draw_move(cell2)
	win.draw_line(line, "black")

	win.wait_for_close()


main()