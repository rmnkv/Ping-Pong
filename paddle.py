from turtle import Turtle, Screen
WEIGHT = 5
HEIGHT = 1

class Paddle(Turtle):
    def __init__(self, STARTING_POSITIONS):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=WEIGHT, stretch_len=HEIGHT)
        self.goto(x=STARTING_POSITIONS[0], y=STARTING_POSITIONS[1])

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
