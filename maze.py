
from graphics import Window 
from cell import Cell
import time
import random

class Maze():
    def __init__(
            self,
            x1:int,
            y1:int,
            num_rows:int,
            num_cols:int,
            cell_size_x:float,
            cell_size_y:float,
            win = None,       
            seed = None
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
        self._break_entrance_and_exit()
        if seed is not None:
            self.seed = random.seed(self.seed)
        self._break_walls_r(0,0)
        self._reset_cells_visited()    
    def _create_cells(self):
        for i in range(self._num_cols):
            self._cells.append([])
            for j in range(self._num_rows ):
                self._cells[i].append(Cell(self._win))
            
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)
       
    
    def _draw_cell(self, i , j): 
        if self._win is None:
            return
        x_start = self._x1 + j * self._cell_size_x
        x_end = x_start + self._cell_size_x 
        y_start = self._y1 + i * self._cell_size_y
        y_end = y_start + self._cell_size_y 
        self._cells[i][j].draw(x_start ,x_end, y_start , y_end)
        self._animate_self()
        return

    def _animate_self(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05) 

    def _break_entrance_and_exit (self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[(self._num_cols - 1)][(self._num_rows - 1)].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1 , self._num_rows -1)

    def _break_walls_r(self,i,j):
        self._cells[i][j].visited = True

        while True:
            possible_directions = self._get_possible_directions(i,j) 

            if len(possible_directions) == 0:
                self._draw_cell(i,j)
                return
            else:
                random_index = random.randrange(len(possible_directions))
                next_cell = possible_directions[random_index]
                ni , nj = next_cell
                self._break_wall(i,j,ni,nj)            
            self._break_walls_r(ni,nj)
    
    def _break_wall_stack(self,i , j):
        stack=[(i,j)]
        self._cells[i][j].visited = True
            
        while stack:
            i,j = stack[-1]
            possible_directions = self._get_possible_directions(i,j)
          
            if possible_directions:
                next_cell = random.choice(possible_directions)
                ni , nj = next_cell
                self._break_wall(i,j,ni,nj)
                self._cells[ni][nj].visited = True
               
                
          
             
    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False
            
    def solve_maze(self):
        result = self._solve_r(0,0)
        return result


    
    def _solve_r(self , i , j):
        if self._cells[i][j] == self._cells[self._num_cols -1][self._num_rows -1 ]:
            return True
        self._animate_self()
        self._cells[i][j].visited = True
        
        if not self._cells[i][j].has_left_wall and j-1 >= 0 and not self._cells[i][j - 1].visited:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            result = self._solve_r(i, j -1)
            if result :
                return True 
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1] , True)



        if not self._cells[i][j].has_right_wall and j+1 < self._num_rows   and not self._cells[i][j + 1].visited:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            result =self._solve_r(i , j + 1)
            if result :
                return True 
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], True)

        if not self._cells[i][j].has_top_wall and i -1 >= 0 and not self._cells[i - 1][j].visited:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            result = self._solve_r(i - 1 , j)
            if result : 
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j] , True)

        if not self._cells[i][j].has_bottom_wall and i+1 < self._num_cols  and not self._cells[i + 1][j].visited:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            result = self._solve_r(i +1 , j)
            if result:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i +1][j], True ) 
        return False
            


    def _get_possible_directions(self, i , j):
        possible_directions = []
        if i > 0 and not self._cells[i-1][j].visited:
            possible_directions.append((i-1,j))
        if i < (self._num_cols - 1) and not self._cells[i+1][j].visited:
            possible_directions.append((i+1,j))
        if j > 0 and not self._cells[i][j-1].visited:
            possible_directions.append((i,j-1))
        if j < (self._num_rows -1) and not self._cells[i][j+1].visited:
            possible_directions.append((i,j+1))
        return possible_directions

    def _break_wall(self,i,j,ni,nj):
        if ni < i :
            if i > 0:
                self._cells[i][j].has_top_wall = False
                self._cells[ni][nj].has_bottom_wall = False
        elif ni > i :
            if i < (self._num_cols -1 ):
                self._cells[i][j].has_bottom_wall = False
                self._cells[ni][nj].has_top_wall = False
        elif nj < j :
            if j > 0:
                self._cells[i][j].has_left_wall = False
                self._cells[ni][nj].has_right_wall = False
        elif nj > j:
            if j < (self._num_rows -1):
                self._cells[i][j].has_right_wall = False
                self._cells[ni][nj].has_left_wall = False
    







         

