import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size and title
window_size = (600, 600)
window_title = "Space Invaders"

# Create the window
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption(window_title)

# Set the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set the player's starting position and speed
player_x = window_size[0] // 2
player_y = window_size[1] - 50
player_speed = 5

# Set the enemy's starting position and speed
enemy_x = random.randint(0, window_size[0])
enemy_y = 50
enemy_speed = 2

# Set the bullet's starting position and speed
bullet_x = 0
bullet_y = player_y
bullet_speed = 10
bullet_fired = False

# Create a font for the score
font = pygame.font.Font(None, 36)

# Set the starting score
score = 0

# Run the game loop
while True:
    # Draw the screen
    screen.fill(black)

    # Draw the player
    pygame.draw.circle(screen, white, (player_x, player_y), 20)

    # Draw the enemy
    pygame.draw.circle(screen, white, (enemy_x, enemy_y), 20)

    # Draw the bullet if it has been fired
    if bullet_fired:
        pygame.draw.circle(screen, white, (bullet_x, bullet_y), 5)

    # Update the player's position based on input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    player_x = max(20, min(player_x, window_size[0] - 20))

    # Update the enemy's position
    enemy_x += enemy_speed
    if enemy_x < 20 or enemy_x > window_size[0] - 20:
        enemy_speed *= -1
        enemy_y += 50

    # Update the bullet's position if it has been fired
    if bullet_fired:
        bullet_y -= bullet_speed
        if bullet_y < 0:
            bullet_fired = False

    pygame.display.update()


