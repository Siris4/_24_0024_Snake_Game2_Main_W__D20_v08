import turtle
from turtle import Turtle, Screen

#main.py controls the entire game
#snake module = snake's appearance and behavior

screen = Screen()

# CONSTANTS:
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]    #will ALWAYS start here, so using Tuples is PERFECT!! Constants = Tuples, so this goes in ALL CAPS!
AMOUNT_OF_PIXELS_SNAKE_MOVES_EACH_FRAME = 20
#to prevent from cheating and doing a 180 turn:
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake:

    def __init__(self):           # extras: shape, pensize=20, color="orange"
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        # self.shape = shape
        # self.pensize = pensize
        # self.color = color

    def create_snake(self):           #creates a new snake, with 3 total segments as the body, to start
        for loop_iteration_position in STARTING_POSITIONS:
            self.add_segment(loop_iteration_position)


    def add_segment(self, position):
        new_segment = Turtle(shape="square")    # this info (and lines below it) was moved from create_snake (above) to the add_segment function definition
        new_segment.pensize(20)
        new_segment.color("orange")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
                                                #This above and this below are used together to add an extra block to the snake body, once passed through a food block.

    def extend_snake_body(self):   #add new segment to the snake.
        self.add_segment(self.segments[-1].position())                         #get ahold of the last segment, and it's position)


    def move(self):     #anytime you're within your Class, you have to put (self) in the parenthesis and a self. in front of any variable names!
        for seg_num in range(len(self.segments) - 1, 0, -1):   #if you want (1, 2, 3), then start=1, stop=3, step=1. BUT in reverse order (3, 2, 1): start=3, stop=1, step=-1. We actually want to go from 2, 1, 0 because of the 3 starting positions and segments[2] seg[1] and seg[0], which we apply here!
            new_x = self.segments[seg_num - 1].xcor()        #get ahold of the x-coordinate of the 2nd to last segment here
            new_y = self.segments[seg_num - 1].ycor()        #get ahold of the y-coordinate of the 2nd to last segment here
            self.segments[seg_num].goto(new_x, new_y)          #get ahold of the last segment here
        self.head.forward(AMOUNT_OF_PIXELS_SNAKE_MOVES_EACH_FRAME)                  #OUTSIDE of the For Loop, get ahold of the first segment, and move that forward, so all the other code trails behind the front moving block.



    # TODO 3: Snake Turning left
    def go_west(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # TODO 4: Snake Turning right
    def go_east(self):
        if self.head.heading() != LEFT:           # careful: head.deading() is a Method
            self.head.setheading(RIGHT)

    def go_up(self):
        if self.head.heading() != DOWN:   #if the current heading is pointed down, it can't move up,
            self.head.setheading(UP)         #if it's any other direction other than down, it is allowed to move up!

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def reset_snake(self):     #we are basically reproducing what the __init__ function does at Initialization. We are going to "Initialize the snake".
        # in order for us to COMPLETELY clear the screen of the previous version snake (which lingers afterwards), you need to send that version to a different location (The turtle segments)
        #so just before we clear rge segments (while we still have access to them), use a for loop to send each of them to a different location (in this case, a location that is off the screen).
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]



    # def reset_board(self):
    #     self.reset_board()