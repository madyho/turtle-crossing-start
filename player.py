from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.reset_player()
        self.finish_line_y = FINISH_LINE_Y
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_player(self):
        self.goto(STARTING_POSITION)
