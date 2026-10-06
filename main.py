import time
from turtle import Turtle, Screen
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle

R_STARTING_POSITIONS = [350, 0]
L_STARTING_POSITIONS = [-350, 0]

screen = Screen()
screen.title("Ping Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)


right_paddle = Paddle(R_STARTING_POSITIONS)
left_paddle = Paddle(L_STARTING_POSITIONS)
ball = Ball()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
game_on = True
scoreboard = Scoreboard()

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 325 or ball.distance(left_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()

    if ball.xcor() < -380:
        scoreboard.l_point()
        ball.reset_position()

    if ball.xcor() > 380:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()


