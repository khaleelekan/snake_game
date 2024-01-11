from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 8, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.point = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write(f"Score :{self.point} ", False, align=ALIGN, font=FONT)

    def write_score(self):
        self.write(f"Score :{self.point} ", False, align="left", font=("Arial", 8, "normal"))

    def add_score(self):
        self.point += 1
        self.clear()
        self.write_score()
