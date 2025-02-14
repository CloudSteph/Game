import pygame
import random
from models.scoop import Scoop
from models.cone import Cone

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (135, 206, 250) # Light blue sky

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ice Cream Catcher")

# Create cone and a test scoop
cone = Cone(WIDTH // 2, HEIGHT - 100)
scoop = Scoop(random.randint(50, WIDTH - 50), 50, random.choice(["vanilla", "chocolate", "strawberry"]))

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Fill screen with background color
    screen.fill(BACKGROUND_COLOR)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move scoop down
    scoop.fall()

    # Get keys for movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        cone.move("left")
    if keys[pygame.K_RIGHT]:
        cone.move("right")

    # Draw objects
    scoop.draw(screen)
    cone.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(60)

# Quit pygame
pygame.quit()