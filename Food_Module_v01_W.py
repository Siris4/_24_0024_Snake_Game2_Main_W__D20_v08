
from turtle import Turtle
import random

class Food(Turtle):
  # SUPER TURTLE CLASS!!!
    def __init__(self):         # Remember: When you initialize a new object from the class, the init gets called.
        # self.food = Turtle()
        super().__init__()         #we need to call the Turtle's init Method inside the food's init's method.
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x_coord = random.randint(-280, 280)
        random_y_coord = random.randint(-280, 280)
        self.goto(random_x_coord, random_y_coord)


    def respawn_food_location(self):
        random_x_coord = random.randint(-280, 280)
        random_y_coord = random.randint(-280, 280)
        self.goto(random_x_coord, random_y_coord)


