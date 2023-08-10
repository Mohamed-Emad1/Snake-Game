import turtle
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):

        self.new_box = []
        self.create_snake()
        self.head = self.new_box[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_square(position)

    def add_square(self, position):
        new_square = Turtle("square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.new_box.append(new_square)

    def extended_snake(self):
        # position
        self.add_square(self.new_box[-1].position())

    def move(self):
        for square_num in range(len(self.new_box) - 1, 0, -1):
            new_x = self.new_box[square_num - 1].xcor()
            new_y = self.new_box[square_num - 1].ycor()
            self.new_box[square_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
