from graphics import Window, Point,Line,Cell
 
 
def main():
    win = Window(800 , 600)

    cell1 = Cell(
                400,
                410,
                300,
                310,
                win,
                False,
                False,
                True,
                True
                )
    cell1.draw()
        
    win.wait_for_close()




if __name__ == '__main__' :
    main()
