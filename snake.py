from turtle import Turtle, Screen
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DIRECTION = {"Up": 90, "Left": 180, "Down": 270, "Right": 0}


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def movement(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].xcor(), self.segments[seg_num - 1].ycor())
        self.segments[0].forward(MOVE_DISTANCE)

    def add_segment(self):
        segment = self.segments[-1].clone()
        self.segments.append(segment)
        segment.backward(20)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def left(self):
        if self.segments[0].heading() != DIRECTION["Right"]:
            self.segments[0].setheading(DIRECTION["Left"])

    def right(self):
        if self.segments[0].heading() != DIRECTION["Left"]:
            self.segments[0].setheading(DIRECTION["Right"])

    def up(self):
        if self.segments[0].heading() != DIRECTION["Down"]:
            self.segments[0].setheading(DIRECTION["Up"])

    def down(self):
        if self.segments[0].heading() != DIRECTION["Up"]:
            self.segments[0].setheading(DIRECTION["Down"])

