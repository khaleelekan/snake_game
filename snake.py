from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.create_new_snake()
        self.move()
        self.segments = []

    def create_new_snake(self):
        for pos in STARTING_POSITIONS:
            new_square = Turtle("square")
            new_square.penup()
            new_square.color("white")
            new_square.goto(pos)
            self.segments.append(new_square)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[seg - 1].xcor()
            y_cor = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x_cor, y_cor)
        self.segments[0].forward(20)
