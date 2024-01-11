from turtle import Turtle, Screen
from snake import Snake
import time
screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

is_on = True
snake = Snake()
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
