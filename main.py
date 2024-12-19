import random
from turtle import Screen
from enimies import Enimies
from enimies_bullet import E_bullets  # Ensure this is imported
from shooter import Shooter

e_block = []
screen = Screen()
screen.tracer(0)
screen.setup(1000, 500)

# Create enemy blocks
for i in range(200, 50, -50):
    for j in range(-100, 150, 50):
        e_block.append(Enimies(j, i))

direction = 1
shooter = Shooter(screen, e_block)


def move_all_enemies():
    global direction
    boundary_reached = False

    # Move each enemy block
    for enemy in e_block:
        if (enemy.e.xcor() + (100 * direction)) > 450 or (enemy.e.xcor() + (100 * direction)) < -450:
            boundary_reached = True

    # If any block reaches the boundary, reverse direction for all
    if boundary_reached:
        direction *= -1

    # Move all blocks in the current direction
    for enemy in e_block:
        enemy.move(direction)

    # Randomly fire a bullet from any enemy
    if e_block:  # Ensure there are enemies
        random_enemy = random.choice(e_block)
        E_bullets(random_enemy.e.xcor(), random_enemy.e.ycor(), screen)

    # Check for collisions (between shooter and enemy bullets, or shooter bullets and enemies)
    shooter.detect_game_over()  # Detect game over condition
    shooter.check_bullet_collisions()  # Check if shooter's bullet hits any enemy

    # Listen for key events
    screen.onkeypress(key="Left", fun=shooter.move_left)
    screen.onkeypress(key="Right", fun=shooter.move_right)
    screen.onkeypress(key="space", fun=shooter.shoot)  # Corrected key symbol

    screen.update()  # Update the screen once all enemies have moved
    screen.ontimer(move_all_enemies, 1500)  # Adjust timing as needed


move_all_enemies()
screen.listen()  # Start listening for key events
screen.exitonclick()
