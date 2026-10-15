import turtle
import random
"""import os 
from turtle import Turtle """

#Part 1: Screen and Sprite
turtle.fd(0) # To show the screen
turtle.speed(0)  #animation speed to max
turtle.bgcolor("black")  #background color
turtle.setundobuffer(1)  #limits and saves memory
turtle.tracer(1)  #speeds up animation/drawing (1-default)


class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        super().__init__()
        self.shape(spriteshape)
        self.speed(0)  #animation speed
        self.penup()
        self.color(color)  #color of the sprite
        self.goto(startx, starty)  #move to the starting point
        self.sprite_speed = 1  #sprite speed set to default

    #Part 2: Speed
    def move(self):
        self.fd(self.sprite_speed)

        #Part3: Boundaries on the screen
        #Boundary Detection - Turns away when it hits the border
        if self.xcor() > 390:
            self.setx(390)  # Sets any value over 390 or 290 back to 290 or 390
            self.rt(60)  # Angle to turn - 60 degrees

        if self.xcor() < -390:
            self.setx(-390)
            self.rt(60)

        if self.ycor() > 290:
            self.sety(290)
            self.rt(60)

        if self.ycor() < -290:
            self.sety(-290)
            self.rt(60)

#Part 4- Defining Collision
    def is_collision(self,other):
        if (other.xcor() - 20) <= self.xcor() <= (other.xcor() + 20) and self.ycor() >= (other.ycor() - 20) and self.ycor() >= (other.ycor() + 20):
            return True
        else:
            return False

#Part 2: Defining Player
class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        super().__init__(spriteshape, color, startx, starty)
        self.sprite_speed = 4
        self.lives = 3

    #Defining methods (moves)
    def turn_left(self):
        self.lt(45)

    def turn_right(self):
        self.rt(45)

    def accelerate(self):
        self.sprite_speed += 1

    def decelerate(self):
        self.sprite_speed -= 1

#Part 4 - Defining enemy
class Enemy(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        super().__init__(spriteshape, color, startx, starty)
        self.sprite_speed = 6
        self.setheading(random.randint(0,360))

#Part 3: Defining methods for the game
class Game:
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing" # playing, over or waiting
        self.pen = turtle.Turtle()
        self.lives = 3

    def draw_border(self):
        #Draw border for screen (800*800)
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto( -400, 300)
        self.pen.pendown()
        for side in range(2):
            self.pen.fd(800)
            self.pen.rt(90)
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()

#Create game object
game = Game()

#Draw the game border
game.draw_border()

#Part 1 -
#Creating sprites
player = Player("triangle", "white", 0, 0)
#Part 4-
enemy  = Enemy ("circle","red",-100,0)

#Part 2 -
# Keyboard Bindings - connecting methods (moves) to keys
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.listen()

#Main game loop
while True:
    player.move()
    #Part 4 -
    enemy.move()

    #Checking for a collision
    if player.is_collision(enemy):
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        enemy.goto(x,y)

turtle.done()
