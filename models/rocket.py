from pygame import *
from pygame.math import *

from shared.configs import *
from models.dna import Dna


class Rocket:
    """
    Rocket Agent,
    Responsible for handling the visualization and genetic details of the rocket
    """

    def __init__(self, visualizer, dna=None):
        self.visualizer = visualizer

        self.pos = Vector2(*ROCKETS_SPAWN_LOC)
        self.dna = dna if dna else Dna()
        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)

        self.is_crashed = False
        self.is_complete = False
        self.fitness = 0

    def update(self, frame_count, world):

        if self.is_crashed:
            return

        # Apply force
        self.acceleration += self.dna.genes[frame_count]

        self.velocity += self.acceleration
        self.pos += self.velocity
        self.acceleration *= 0

        # Check collisions
        if world.check_target_collision(self.pos):
            self.is_crashed = True
            self.is_complete = True
        elif world.check_world_collision(self.pos) or \
                world.check_obstacles_collision(self.pos):
            self.is_crashed = True

    def calc_fitness(self):
        """ The rocket fitness function """

        dist_to_target = self.pos.distance_to(
            Vector2(*TARGET_LOCATION))
        self.fitness = 1 if dist_to_target is 0 \
            else (1 / dist_to_target)

        # Reward system
        if self.is_complete:
            self.fitness *= 0.1
        elif self.is_crashed:
            self.fitness *= 0.05
        else:
            self.fitness *= 0.01

    def normalize_fitness(self, normalization_value):
        """
        Normalization is a scaling technique in Machine Learning applied during data preparation
        to change the values of numeric columns in the dataset to use a common scale
        """

        self.fitness /= normalization_value

    def draw(self):
        # Create surface and fill it with white color
        rocket_surface = Surface(ROCKET_SIZE, SRCALPHA)
        rocket_surface.fill(self._get_rocket_color())
        size = rocket_surface.get_size()

        angle = self.velocity.angle_to(Vector2(1, 0))
        rocket_surface = transform.rotate(rocket_surface, angle + 90)

        self.visualizer.draw_surface(rocket_surface, (self.pos.x - (size[0] / 2), self.pos.y - (size[1] / 2)))

    def _get_rocket_color(self):
        if self.is_complete:
            return ROCKET_COLOR_COMPLETED
        elif self.is_crashed:
            return ROCKET_COLOR_CRASHED
        elif self.dna.is_mutated:
            return ROCKET_COLOR_MUTATED
        else:
            return ROCKET_COLOR
