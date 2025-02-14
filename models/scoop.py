import pygame
import random

class Scoop:
    """Represents an ice cream scoop falling from the sky."""

    SCOOP_COLORS = {
        "vanilla": (255, 229, 180),
        "chocolate": (123, 63, 0),
        "strawberry": (255, 105, 180),
        "mint": (152, 255, 152),
        "blueberry": (70, 130, 180)
    }

    def __init__(self, x, y, flavor):
        """
        Initialize  an ice cream scoop.

        :param x: Starting x-position
        :param y: Starting y-position
        :param flavor: Type of scoop (e.g., vanilla, chocolate)
        """
        self.x = x
        self.y = y
        self.flavor = flavor
        self.color = self.SCOOP_COLORS.get(flavor, (255, 255, 255)) # Default white if not found
        self.radius = 25 # Size of scoop
        self.speed = random.uniform(2.5, 4.5) # Randomized falling speed

    def fall(self):
        """Moves the scoop downward"""
        self.y += self.speed

    def draw(self, screen):
        """Draws the scoop on the screen."""
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)