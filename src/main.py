from graphics import Window, Point, Line
from cell import Cell
from maze import Maze

def main():
	win = Window(800, 600)
	maz = Maze(5,5,10,10,50,50,win)
	maz._create_cells()
	win.wait_for_close()

if __name__ == "__main__":
	main()