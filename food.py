import random
from turtle import Turtle


class Food(Turtle):             #inheretence    Food extends Turtle ==>java
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)            # keep food to 10 x 10
        self.color("magenta")
        # self.speed("fastest")
        self.refresh()

    def refresh(self):
        new_x = random.randint(-280, 280)
        new_y = random.randint(-280, 280)

        self.goto(new_x, new_y)
