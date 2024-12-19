from turtle import Turtle

class S_bullet:
    instances = []  # Keep track of all bullets fired by the shooter

    def __init__(self, x, y, screen):
        self.b = Turtle()
        self.b.shape("square")
        self.b.turtlesize(0.5, 0.2)
        self.b.penup()
        self.b.goto(x, y)
        self.screen = screen
        S_bullet.instances.append(self)  # Add the bullet to the instances list
        self.move_bullet()

    def move_bullet(self):
        def move():
            new_y = self.b.ycor() + 20  # Move upwards step by step
            self.b.goto(self.b.xcor(), new_y)
            if new_y < 250:  # Keep moving until the bullet is off-screen
                self.screen.ontimer(move, 700)  # Adjust the delay for smooth movement
            else:
                self.b.hideturtle()  # Hide the bullet when it moves off-screen
                S_bullet.instances.remove(self)  # Remove bullet from instances list

        move()

    def detect_collision(self, enemy):

        if self.b.distance(enemy.e) < 30:
            enemy.e.hideturtle()  # Hide enemy block when hit
            return True
        return False
