
from graphics import Window 
from cell import Cell
import time

class Maze():
    def __init__(
            self,
            x1:int,
            y1:int,
            num_rows:int,
            num_cols:int,
            cell_size_x:float,
            cell_size_y:float,
            win = None       
        ) -> None:
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
    
    def _create_cells(self):
        for i in range(self._num_cols):
            self._cells.append([])
            for j in range(self._num_rows ):
                self._cells[i].append(Cell(self._win))
                self._draw_cell(i,j)
        return
    
    def _draw_cell(self, i , j): 
        if self._win is None:
            return
        x_start = (self._cell_size_x * j) + self._x1
        x_end = (self._cell_size_x * j) + self._cell_size_x + self._x1
        y_start = (self._cell_size_y * i) + self._y1
        y_end = (self._cell_size_y * i) + self._cell_size_y +self._y1
        self._cells[i][j].draw(x_start ,x_end, y_start , y_end)
        self._animate_self()
        return



    def _animate_self(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05) 
