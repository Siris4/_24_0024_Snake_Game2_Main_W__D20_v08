
from turtle import Turtle

#CONSTANTS:
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        with open("data.txt") as data:    #yes, you can insert "with open"... into an Initialization phase, as an attribute.
            contents = data.read()  # you must indent!!
        self.high_score = int(contents)    #however, if you close out of the program, the high score gets reset to 0, when it is ran as a fresh program again.
        self.color('white')
        self.goto(0, 270)
        self.write_the_scoreboard()


    def write_the_scoreboard(self):
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)


    def update_score(self):
        self.clear()
        self.score += 1
        self.write_the_scoreboard()


    # def game_over_display(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER DUDE.", move=False, align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:  # mode="w"    (w stands for write)
                contents = file.write(f"{self.high_score}")
        self.score = 0
        self.score -= 1
        self.update_score()




