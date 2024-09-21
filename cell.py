from graphics import Line, Point

 
class Cell():
    def __init__(self,  win = None) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True 
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False 

    def draw(self , x1:int ,x2:int ,y1:int ,y2:int):
        if self._win == None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        left_wall = Line(Point(x1 ,y1),Point(x1,y2))
        right_wall = Line(Point(x2,y1),Point(x2,y2))
        bottom_wall = Line(Point(x1,y2),Point(x2,y2))
        top_wall = Line(Point(x1,y1),Point(x2,y1))
        
        if self.has_left_wall:
            self._win.draw_line(left_wall)
        else:
            self._win.draw_line(left_wall,"white")

        if self.has_right_wall:
            self._win.draw_line(right_wall)
        else:
            self._win.draw_line(right_wall , "white")

        if self.has_bottom_wall:
            self._win.draw_line(bottom_wall )
        else:
            self._win.draw_line(bottom_wall, "white")
        
        if self.has_top_wall:
            self._win.draw_line(top_wall)
        else:
            self._win.draw_line(top_wall , "white")
        return

    def draw_move(self , to_cell , undo:bool = False):
        l = Line(self.center_point(),to_cell.center_point())
        color = "red" if not undo  else "grey" 
        self._win.draw_line(l, color )

    def center_point(self):
        x = 0
        y = 0
        if self._x1 is not None and self._x2 is not None :
            x = (self._x2 + self._x1) /2
        else:
            x = self._x1 if self._x1 is not None else self._x2

        if self._y1 is not None and self._y2 is not None:
            y = (self._y2 + self._y1) /2 
        else:
            y = self._y1 if self._y1 is not None else self._y2 

        center_point = Point(x,y)
        return center_point




