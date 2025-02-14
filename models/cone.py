import pygame

class Cone:
    """Represents the player's ice cream cone."""

    def __init__(self, x, y):
        """
        Initialize the cone.

        :param x: Starting x-position
        :param y: Fixed y-position
        """
        self.x = x
        self.y = y
        self.width = 60
        self.height = 40
        self.color = (255, 165, 0)  # Orange for a waffle cone
        self.speed = 6
        self.caught_scoops = []

    def move(self, direction):
        """Moves the cone left or right."""
        if direction == "left":
            self.x -= self.speed
        elif direction == "right":
            self.x += self.speed

    def catch_scoop(self, scoop):
        """Adds a caught scoop to the cone."""
        self.caught_scoops.append(scoop)

    def draw(self, screen):
        """Draws the cone as a downward-facing triangle to hold scoops."""
        pygame.draw.polygon(screen, self.color, [
            (self.x, self.y + self.height), # 🔽Bottom point (facing downward)
            (self.x - self.width // 2, self.y), # ⏴ Left point (base)
            (self.x + self.width // 2, self.y) # ⏵ Right point (base)
        ])

        # Draw stacked scoops
        for i, scoop in enumerate(self.caught_scoops):
            scoop_x = self.x
            scoop_y = self.y - self.height - (i + 1) * 35  # Stack scoops *above* the cone
            pygame.draw.circle(screen, scoop.color, (scoop_x, scoop_y), scoop.radius)