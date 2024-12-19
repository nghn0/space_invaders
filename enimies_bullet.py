from turtle import Turtle


class E_bullets:
    instances = []  # Keep track of all enemy bullets

    def __init__(self, x, y, screen):
        self.b = Turtle()
        self.b.shape("square")
        self.b.color("red")
        self.b.turtlesize(0.5, 0.2)  # Adjust size to make it bullet-like
        self.b.penup()
        self.b.goto(x, y)  # Start at the given position
        self.screen = screen
        E_bullets.instances.append(self)  # Add to the list of active enemy bullets
        self.move_bullet()

    def move_bullet(self):
        def move():
            new_y = self.b.ycor() - 20  # Move downward step by step
            self.b.goto(self.b.xcor(), new_y)
            if new_y > -250:  # Keep moving until the bullet is off-screen
                self.screen.ontimer(move, 700)  # Adjust the delay for smooth movement
            else:
                self.b.hideturtle()  # Hide the bullet when it moves off-screen
                E_bullets.instances.remove(self)  # Remove from the active list

        move()
