from turtle import*
import turtle
class Square(Turtle):
    def __init__(self,size,color):
        Turtle.__init__(self)
        self.shapesize(size)
        self.shape("square")
        self.color(color)

#s1= Square(10,"red")
turtle.register_shape("hexagon",((50,50),(75,25),(75,0),(50,-50),(25,0),(25,25)))

class Hexagon(Turtle):
    def __init__(self,size,color):
        Turtle.__init__(self)
        self.shapesize(size)
        self.color(color)
        self.shape("hexagon")

hexagon1= Hexagon(10,"blue")


        
