from graphics import *

def main():
    win = GraphWin()

    c = Circle( Point( 40, 75 ), 30 )
    c.setOutline( 'blue' )
    c.setFill( 'blue' )

    r = Rectangle( Point( 80, 30 ), Point( 140, 140 ))
    r.setFill( 'orange' )
    r.setOutline( 'orange' )

    c_shadow = c.clone()
    c_shadow.move(4, 4)
    c_shadow.setOutline( 'lightgrey' )
    c_shadow.setFill( 'lightgrey' )

    r_shadow = r.clone()
    r_shadow.move(4, 4)
    r_shadow.setOutline( 'lightgrey' )
    r_shadow.setFill( 'lightgrey' )

    def makeShadow(shape):
        if shape == Circle:
            c_shadow.draw(win)
            c.draw( win )
        else:
            r_shadow.draw(win) 
            r.draw( win )
    makeShadow(Rectangle)
    makeShadow(Circle)

main()