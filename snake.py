from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
jim = Turtle()
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_new_snake()
        self.move()
        self.head = self.segments[0]

    def create_new_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, pos):
        new_square = Turtle("square")
        new_square.penup()
        new_square.color("white")
        new_square.goto(pos)
        self.segments.append(new_square)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[seg - 1].xcor()
            y_cor = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x_cor, y_cor)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
