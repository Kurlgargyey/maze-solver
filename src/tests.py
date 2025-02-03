import unittest
from maze import Maze

class BasicMazeTests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )

    def test_maze_create_cells_with_positions(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(50, 50, num_rows, num_cols, 15, 15)
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(m1._x1, 50)
        self.assertEqual(m1._y1, 50)
        self.assertEqual(m1._cells[5][3]._x1, 50+5*15)

class EntryExitTests(unittest.TestCase):
    def test_entry_exit_created(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(50, 50, num_rows, num_cols, 15, 15)
        self.assertFalse(m1._cells[0][0].has_top_wall)
        self.assertFalse(m1._cells[-1][-1].has_bottom_wall)

class BreakWallsTests(unittest.TestCase):
    def test_loop_finishes(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(50, 50, num_rows, num_cols, 15, 15)
        m1._break_walls_r(0, 0)
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()