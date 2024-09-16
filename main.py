from graphics import Window, Point,Line
 
 
def main():
    win = Window(800 , 600)
    point_a = Point(3 ,5)
    point_b = Point(10 ,10)
    point_c = Point(400 ,400)
    point_d = Point(500 ,500)

    line_a_b = Line(point_a,point_b)
    line_c_d = Line(point_c,point_d)
    win.draw_line(line_a_b,"black")
    win.draw_line(line_c_d , "red")
    win.wait_for_close()




if __name__ == '__main__' :
    main()
