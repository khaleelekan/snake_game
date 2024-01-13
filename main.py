from turtle import Turtle, Screen
from snake import Snake
from scoreboard import Score
from food import Food
import time
screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
score = Score()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
is_on = True

while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# detect collision with food
    if snake.head.distance(food) < 15:
        score.add_score()
        snake.extend()
        food.refresh()
# detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        is_on = False
        score.game_over()
# detect collision with tail
for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
        is_on = False
        score.game_over()

screen.exitonclick()
