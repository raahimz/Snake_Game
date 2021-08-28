from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
facing_top = False
facing_down = False
facing_left = False
facing_right = True


class Snake:

    def __init__(self):
        self.segments = []
        self.create_segments()

    def create_segments(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('lightgreen')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            x_cord = self.segments[segment - 1].xcor()
            y_cord = self.segments[segment - 1].ycor()
            self.segments[segment].goto(x_cord, y_cord)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        global facing_right
        global facing_top
        global facing_left
        if facing_right or facing_left:
            self.segments[0].setheading(90)
            facing_right = False
            facing_top = True
            facing_left = False
        else:
            return None

    def down(self):
        global facing_right
        global facing_left
        global facing_down
        if facing_right or facing_left:
            self.segments[0].setheading(270)
            facing_right = False
            facing_down = True
            facing_left = False
        else:
            return None

    def left(self):
        global facing_top
        global facing_down
        global facing_left
        if facing_top or facing_down:
            self.segments[0].setheading(180)
            facing_top = False
            facing_left = True
            facing_down = False
        else:
            return None

    def right(self):
        global facing_top
        global facing_down
        global facing_right
        if facing_top or facing_down:
            self.segments[0].setheading(0)
            facing_top = False
            facing_right = True
            facing_down = False
        else:
            return None
