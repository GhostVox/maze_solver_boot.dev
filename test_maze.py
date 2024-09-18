import unittest

from maze import Maze
from cell import Cell


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0,0,num_rows,num_cols,10,10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    def test_maze_win(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(800,600,num_rows,num_cols,10,10)
        self.assertEqual(m1._win , None)

        self.assertEqual(m1._x1 , 800)
        self.assertEqual(m1._y1 , 600)

    def test_cell_center_point(self):
        fake_win = {"_x1":0 , "_x2":10 , "_y1":0 , "_y2":10}

        cell = Cell(fake_win)
        cell._x1 , cell._x2 , cell._y1 , cell._y2 = 2 , 10 ,0 , 10
        
        cell_2 = Cell(fake_win)
        cell_2._x1 , cell_2._x2 , cell_2._y1 , cell_2._y2 = None , 10 ,None , 10

        point_2 = cell_2.center_point()
        self.assertEqual(point_2.x , 10)
        self.assertEqual(point_2.y , 10)
        
    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )


if __name__ == "__main__":
    unittest.main()
