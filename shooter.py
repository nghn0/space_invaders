import time
from turtle import Turtle
from shooter_bullet import S_bullet
from enimies_bullet import E_bullets

class Shooter:
    def __init__(self, screen, enemies):
        self.s = Turtle()
        self.s.penup()
        self.s.turtlesize(2)
        self.s.setheading(90)
        self.s.goto(0, -200)
        self.screen = screen
        self.enemies = enemies
        self.score = 0
        self.game_active = True  # Flag to indicate if the game is running

    def move_left(self):
        if self.game_active and self.s.xcor() > -450:
            new_x = self.s.xcor() - 20
            self.s.goto(new_x, self.s.ycor())

    def move_right(self):
        if self.game_active and self.s.xcor() < 450:
            new_x = self.s.xcor() + 20
            self.s.goto(new_x, self.s.ycor())

    def shoot(self):
        if self.game_active:
            # Create a bullet at the shooter's position
            S_bullet(self.s.xcor(), self.s.ycor(), self.screen)

    def detect_game_over(self):
        for enemy_bullet in E_bullets.instances:  # Loop through all enemy bullets
            if self.s.distance(enemy_bullet.b) < 20:  # Check for collision
                print("Game Over")
                self.s.hideturtle()  # Hide the shooter turtle to avoid overlapping
                self.s.penup()
                self.s.goto(0, 0)  # Move the turtle to the center
                self.s.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
                self.game_active = False  # Set game flag to inactive
                return True
        return False

    def check_bullet_collisions(self):
        if not self.game_active:
            return False
        for bullet in S_bullet.instances:
            for enemy in self.enemies:
                if bullet.detect_collision(enemy):  # If the bullet hits an enemy
                    self.enemies.remove(enemy)  # Remove the enemy from the list
                    bullet.b.hideturtle()  # Hide the bullet
                    self.score += 1
                    return True
        return False
