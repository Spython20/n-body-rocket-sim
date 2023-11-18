import pygame.draw
import vector
from vector import Vector

class Planet:
    def __init__(self, position: Vector, radius: float, color=(255, 255, 255)):
        self.position = Vector.copy(position)

    def update(self, data, body, time):
        self.position = data[body]["x"][time]

    def draw(self, screen):
        top_left_position = self.position - self.radius
        pygame.draw.circle(screen, self.color, top_left_position.make_int_tuple(), 10)
