from turtle import Turtle
from turtle import *
import turtle
import time
import random
from balltry import Ball
import math
#import pygame

#pygame.init()

#size = [turtle.getcanvas().winfo_width()/2 , turtle.getcanvas().winfo_height()/2]

#screen = pygame.display.set_mode(size)

#done = False
#background_position = [0, 0]
#background_image = pygame.image.load("agario_bg.png").convert()

#while not done:
 #   for event in pygame.event.get() :
  #      if event.type == pygame.QUIT:
   #         done = True
   
   # screen.blit(background_image, background_position)

    #pygame.display.flip()

    #clock.tick(60)

#backgroun = games,load_image("agario_bg.png", transparent = False)

#my_screen.set_background(backgroun)


##screen = turtle.Screen()
##screen.setup(turtle.getcanvas().winfo_width()/2 , turtle.getcanvas().winfo_height()/2)
##time.sleep(2)
##screen.bgpic('agario_bg.gif')







turtle.tracer(0)
turtle.hideturtle()
turtle.penup()
turtle.goto(-320,250)
RUNNING=True
SLEEP=0.01
#s = 0
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2

MY_BALL=Ball(5,5,10,20,30,"red")

NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=40
MINIMUM_BALL_DX=-5
MAXIMUM_BALL_DX=5
MINIMUM_BALL_DY=-5
MAXIMUM_BALL_DY=5

BALLS=[]



wn=turtle.Screen()
wn.bgcolor("lightblue")
speed=1
wn.tracer(2)


#Score Variable
score=0
#Turtle Player
spaceship= turtle.Turtle()
spaceship.pensize(1)
spaceship.color("red")
spaceship.penup()
turtle.delay(3)
spaceship.shapesize(1,1)
add=1

#Create Goals
maxpoints = 6
points = []

##for count in range(maxpoints):
##    points.append(turtle.Turtle())
##    points[count].color("green")
##    points[count].shape("circle")
##    points[count].penup()
##    points[count].goto(random.randint(-300,300), random.randint(-200,200))

#Border
border = turtle.Turtle()
border.penup()
border.goto(-330,-270)
border.pendown()
border.pensize(5)
border.color("darkblue")
for side in range(2):
    border.forward(655)
    border.left(90)
    border.forward(540)
    border.left(90)

border.hideturtle()
spaceship.hideturtle()



#Functions
##def left():
##    spaceship.left(30)
##def right():
##    spaceship.right(30)
##
##def increasespeed():
##    global speed
##    speed += 1
##
##def decreasespeed():
##    global speed
##    speed -= 1
##
##def iscollision(turtle1,turtle2):
##    collect = math.sqrt(math.pow(turtle1.xcor()-turtle2.xcor(),2)+ math.pow(turtle1.ycor()-turtle2.ycor(),2))
##    if collect <20:
##        return True
##    else:
##        return False








for i in range (NUMBER_OF_BALLS):
    x=random.randint(int(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS) , int(SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))
    y=random.randint(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS) , int(SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS))
    dx=random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
    dy=random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
    radius=random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
    color=(random.random(),random.random(),random.random())
    ball2=Ball(x,y,dx,dy,radius,color)
    BALLS.append(ball2)

def move_all_balls():
    for i in BALLS:
        i.move( SCREEN_WIDTH ,SCREEN_HEIGHT)

def collide(ball_1,ball_2):
    if ball_1==ball_2:
        return False
    D = math.sqrt(math.pow((ball_1.xcor()-ball_2.xcor()),2) + math.pow((ball_1.ycor()-ball_2.ycor()),2))
    if D+10<=ball_1.r+ball_2.r:
        return True
    else:
        return False

def check_all_balls_collision():
    for ball_1 in BALLS:
        for ball_2 in BALLS:
            if collide(ball_1,ball_2):
                b1_r=ball_1.r
                b2_r=ball_2.r
                if (b1_r<b2_r):
                    x=random.randint(int(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS) ,int( SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))
                    y=random.randint(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS) ,int( SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS))
                    ball_1.goto(x, y)
                    ball_1.dx=(random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX))
                    ball_1.dy=(random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY))
                    ball_1.r=(random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS))
                    ball_1.color=(random.random(),random.random(),random.random())
                    ball_1.shapesize(ball_1.r/10)
                    ball_2.r+=1
                    ball_2.shapesize(ball_2.r/10)
                else:
                    x=random.randint(int(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS) , int(SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))
                    y=random.randint(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS) ,int( SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS))
                    ball_2.goto(x, y)
                    ball_2.dx=(random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX))
                    ball_2.dy=(random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY))
                    ball_2.r=(random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS))
                    ball_2.color=(random.random(),random.random(),random.random())
                    ball_2.shapesize(ball_2.r/10)
                    ball_1.r+=1
                    ball_1.shapesize(ball_1.r/10)
				
					
					
s= 0
def check_myball_collisions():
    
    for i in BALLS:
        if collide(i,MY_BALL):
            the_ball_rad=i.r
            
            if the_ball_rad > MY_BALL.r:
                #return False
                exitonclick()
            
            else:
                turtle.clear()
                s+=1
                global s
                
                
                turtle.write("my score: "+str(s))
                
                x=random.randint(int(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS) ,int( SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))
                y=random.randint(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS) ,int( SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS))
                i.goto(x, y)
                i.dx=(random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX))
                i.dy=(random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY))
                i.r=(random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS))
                i.color=(random.random(),random.random(),random.random())
                i.shapesize(i.r/10)
                MY_BALL.r+=1
                MY_BALL.shapesize(MY_BALL.r/10)



##while True:
##    if collide(i,MY_BALL):
##        turtle.clear()
##        s += 1
##        turtle.write(s)





def movearound(event):
    MY_BALL.goto(event.x-SCREEN_WIDTH,SCREEN_HEIGHT-event.y)

turtle.getcanvas().bind("<Motion>", movearound)
turtle.getscreen().listen()

while (RUNNING==True):
    #if SCREEN_WIDTH != turtle.getcanvas().winfo_width()/2 and SCREEN_HEIGHT!=turtle.getcanvas().winfo_height()/2 :
        #SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
        #SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
    move_all_balls()
    check_all_balls_collision()    #MY_BALL.move(SCREEN_WIDTH,SCREEN_HEIGHT)
    check_myball_collisions()
    turtle.update()
    time.sleep(SLEEP)
   

turtle.mainloop()

    
