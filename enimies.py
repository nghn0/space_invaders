from turtle import Turtle

class Enimies:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.e = Turtle()
        self.e.shape("square")
        self.e.penup()
        self.enimies_block()

    def enimies_block(self):
        self.e.goto(self.x, self.y)

    def move(self, direction):
        # Move in the current direction (passed from `move_all_enemies`)
        new_x = self.e.xcor() + (100 * direction)
        self.e.goto(new_x, self.e.ycor())
