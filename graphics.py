from tkinter import Tk, Canvas , BOTH

class Point():
    def __init__(self,x:int , y:int) -> None:
        self.x = x
        self.y = y 
    

class Line():
    def __init__(self, point1:Point , point2:Point) -> None:
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas:Canvas , fill_color:str):
        canvas.create_line(self.point1.x,
                           self.point1.y ,
                           self.point2.x,
                           self.point2.y,
                           fill=fill_color,
                           width= 2
                           )

        
class Window():
    def __init__(self , width , height):
        self.__root = Tk()
        self.__root.title("Maze solver")
        self.__canvas = Canvas(self.__root , width= width , height= height , background="white") 
        self.__canvas.pack(fill=BOTH , expand=1)
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("window closed...")        
    def close(self):
        self.running = False
        self.__root.destroy()

    def draw_line(self , line:Line , fill_color:str="black"):
        line.draw(self.__canvas , fill_color)


class Cell():
    def __init__(self, 
                 _x1:int, 
                 _x2:int, 
                 _y1:int, 
                 _y2:int, 
                 _win:Window,
                 has_left_wall:bool = True,
                 has_right_wall:bool= True,
                 has_top_wall:bool = True, 
                 has_bottom_wall:bool = True,
                 ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall 
        self.has_bottom_wall = has_bottom_wall
        self._x1 = _x1
        self._x2 = _x2
        self._y1 = _y1
        self._y2 = _y2
        self._win = _win
    
    def draw(self):
        if self.has_left_wall:
            l =Line(Point(self._x1,self._y1),Point(self._x1,self._y2))
            self._win.draw_line(l)
        if self.has_right_wall:
            l =Line(Point(self._x2,self._y1),Point(self._x2,self._y2))
            self._win.draw_line(l)
        if self.has_bottom_wall:
            l =Line(Point(self._x1,self._y2),Point(self._x2,self._y2))
            self._win.draw_line(l)
        if self.has_top_wall:
            l =Line(Point(self._x1,self._y1),Point(self._x2,self._y1))
            self._win.draw_line(l)







