
from turtle import Turtle, Screen
import time

# game_on = False

snake = Turtle()
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Siris's Snake Game")    #lables the Title of the pop-up window!

starting_positions = [(0, 0), (-20, 0), (-40, 0)]    #will ALWAYS start here, so using Tuples is PERFECT!!
snake_segments_list = []

# TODO 1: Create the Snake Body
# 3 squares, which are going to be turtles

# x_coords = 0
# y_coords = 0

for snake_block_body_loop_iteration in starting_positions:
    new_body_segment_for_snake = Turtle(shape="square")
    snake.pensize(20)
    new_body_segment_for_snake.color("orange")
    new_body_segment_for_snake.penup()
    new_body_segment_for_snake.goto(snake_block_body_loop_iteration)
    snake_segments_list.append(new_body_segment_for_snake)



game_on = True

while game_on:
    screen.update()  #if we move this update Method OUTSIDE of the for loop (just below), it basically waits for ALL segments to move forwards first, and THEN generates a screen refresh.
    time.sleep(0.2)  #also, instead of having it delay by 1 second for each SEGMENT individually (as originally placed in the for loop below), change it to 1 sec, after ALL segments have officially shifted, to make this go by a little faster.
                          # right now, our segments are not linked, they are indivially doing their own object instance motions! The first block would turn, but the other 2 would continue to move forward in a straight line.
                                # so ideally, we want them to all be linked together, so we could have segment[2] take over for segment[1]'s spot, and seg[1] take over for the seg[0] spot. Then we control the first segment, where it moves forwards, and the rest follows!
                #so we basically begin a loop, starting from the end, and going to the #1 segment (head of the snake) - reverse order

    #preserve below code (for now), and comment it here, this replace that with accurate code (since range function derives from the C language)
    # for seg_num in range(start=2, stop=0, step=-1):     #Reverse order (2, down to 0)
    # for seg_num in range(start=len(snake_segments_list) - 1, stop=0, step=-1):    #because Lists start at 0, we need to subtract 1 from the length of the list, to get the proper location. Also, because range does not accept those Keyword arguments, we should remove them, and just keep the values as the parameters only, leaving it with the final code (shown just below): (length may vary, which is why we don't loop over 3 anymore)
    for seg_num in range(len(snake_segments_list) - 1, 0, -1):   #if you want (1, 2, 3), then start=1, stop=3, step=1. BUT in reverse order (3, 2, 1): start=3, stop=1, step=-1. We actually want to go from 2, 1, 0 because of the 3 starting positions and segments[2] seg[1] and seg[0], which we apply here!
         new_x = snake_segments_list[seg_num - 1].xcor()        #get ahold of the x-coordinate of the 2nd to last segment here
         new_y = snake_segments_list[seg_num - 1].ycor()        #get ahold of the y-coordinate of the 2nd to last segment here
         snake_segments_list[seg_num].goto(new_x, new_y)          #get ahold of the last segment here
                                                            #we still need to move the other blocks in FRONT of the final one, to their proper positions.
    snake_segments_list[0].forward(20)                  #OUTSIDE of the For Loop, get ahold of the first segment, and move that forward, so all the other code trails behind the front moving block.
    # snake_segments_list[0].left(90)

    head_of_snake = snake_segments_list[0]


    def move_forwards():
        head_of_snake.forward(20)


    # TODO 2: S to go Backwards
    def move_backwards():
        head_of_snake.backward(20)


    # TODO 3: A to go Counter-Clockwise
    def rotate_counter_clockwise():
        head_of_snake.left(90)


    # TODO 3: A to go Counter-Clockwise
    def rotate_clockwise():
        head_of_snake.right(90)



    # def shake_etch_a_sketch():
    #     tod.clear()
    #     tod.penup()
    #     tod.home()
    #     tod.pendown()
        # could also use tod.reset() for all of these, but currently it's safer, longer term to preserve variable data.


    screen.listen()  # it must listen first before triggering functions with key-typing
    # to trigger the function in the moment a key is pressed, remove the additional ()  !!
    screen.onkey(fun=move_forwards, key="Up")
    screen.onkey(fun=move_backwards, key="Down")
    screen.onkey(fun=rotate_counter_clockwise, key="Left")
    screen.onkey(fun=rotate_clockwise, key="Right")
    # screen.onkey(fun=shake_etch_a_sketch, key="r")

screen.exitonclick()