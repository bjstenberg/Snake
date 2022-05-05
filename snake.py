from turtle import Turtle
# create a constant
# Create a snake body three squares
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
# constant to move
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.shapes = []
        self.create_snake()
        self.head = self.shapes[0]

    # create new segments / shapes
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_snake(position)

    def add_snake(self, position):
        new_shape = Turtle("square")
        new_shape.color("white")
        new_shape.penup()
        new_shape.goto(position)
        self.shapes.append(new_shape)

    def reset(self):
        for shape in self.shapes:
            shape.goto(1000, 1000)
        self.shapes.clear()
        self.create_snake()
        self.head = self.shapes[0]

    def extend(self):
        # add new shape to snake.
        self.add_snake(self.shapes[-1].position())

    def move(self):
        for shape_num in range(len(self.shapes) - 1, 0, -1):
            new_x = self.shapes[shape_num - 1].xcor()
            new_y = self.shapes[shape_num - 1].ycor()
            self.shapes[shape_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

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








