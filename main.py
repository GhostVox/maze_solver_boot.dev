from graphics import Window
from cell import Cell
 
 
def main():
    win = Window(800 , 600)

    cell1 = Cell(win)
    cell1.has_left_wall = False
    cell1.has_right_wall = False
    cell2 = Cell( win )
    cell2.has_left_wall = False
    cell2.has_bottom_wall = False
    cell1.draw(400 , 410 , 300 , 310)
    cell2.draw(410 , 420 , 300 ,310)
    win.wait_for_close()




if __name__ == '__main__' :
    main()
