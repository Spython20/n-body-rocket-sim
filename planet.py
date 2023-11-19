import pygame.draw
import vector
from vector import Vector

class Planet:
    def __init__(self, position: Vector, radius: float, color=(255, 255, 255)):
        self.position = Vector.copy(position)
        self.radius = radius
        self.color = color

    def update(self, data, body, time):
        self.position = data[time]['x'][body]

    def draw(self, screen):
        top_left_position_x = self.position.x - self.radius
        top_left_position_y = self.position.y - self.radius

        pygame.draw.circle(screen, self.color, (top_left_position_x, top_left_position_y), 10)
