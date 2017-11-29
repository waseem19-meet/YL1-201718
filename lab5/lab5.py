from turtle import*
import turtle
import random 
## Excercise 1

class Square(Turtle):
    def __init__(self,size,color,speed):
        Turtle.__init__(self)
        self.shapesize(size)
        self.shape("square")
        self.color(color)
        self.speed(speed)

    def teleport(self):
        self.goto(random.randint(0,1000),random.randint(0,1000))
                                                       
s1= Square(10,"red",5)
s1.teleport()

## Excercise 2

class Hexagon(Turtle):
    def __init__(self,size):
        Turtle.__init__(self)
        self.begin_poly()
        for i in range(6):
            self.penup()
            self.forward(10)
            self.right(60)
        self.end_poly()
        self.shapesize(size)
        register_shape('hexagon',self.get_poly())
        self.shape("hexagon")

hexagon1= Hexagon(10)





        
