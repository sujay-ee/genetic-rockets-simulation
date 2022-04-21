import operator

from shared.configs import *
from services.visualizer import Visualizer
from services.world import World
from services.population import Population


class Controller:
    """
    Controller, the central processing hub,
    Responsible for handling the visualizer and other services
    """

    def __init__(self):
        self.visualizer = Visualizer()
        self.world = World(self.visualizer)
        self.population = Population(self.visualizer, self.world)

        self.is_paused = False
        self.frame_count = 0
        self.generation_count = 0
        self.num_completed_rockets = 0

    def draw(self):

        # Reset the simulation window
        self.visualizer.reset()

        # Draw world and rocket population
        self.world.draw()
        self.population.draw()

        # Display simulation statistics
        self._draw_simulation_stats()

        # Repaint all draw calls onto the window
        self.visualizer.repaint()

    def update(self):

        # Update pygame clock
        self.visualizer.clock_tick()

        # Handle mouse and keyboard inputs
        self.is_paused, mouse_events = self.visualizer.get_events()
        if mouse_events:
            self._create_obstruction(mouse_events[0], mouse_events[1])

        if self.is_paused:
            return

        self.frame_count += 1
        self.frame_count %= ROCKET_LIFESPAN

        # frame count == 0 -> end of rocket lifecycle
        if self.frame_count == 0:
            self._reset_generation()
            return

        # Update rockets
        self.population.update(self.frame_count)

    def _reset_generation(self):

        # End current generation
        best_fitness, self.num_completed_rockets = self.population.end_current_generation()
        # print("Gen:", self.generation_count, "Fitness:", best_fitness,
        #       "Complete:", self.num_completed_rockets)

        # Start a new generation
        self.generation_count += 1
        self.population.start_new_generation(best_fitness)

    def _create_obstruction(self, start_pos, end_pos):
        self.world.create_obstacle(start_pos, end_pos)

    def _draw_simulation_stats(self):
        self.visualizer.show_text(
            SIM_STATS_POSITION, "Gen: " + str(self.generation_count))
        self.visualizer.show_text(
            tuple(map(operator.add, SIM_STATS_POSITION, (0, 20))),
            "Complete: " + str(self.num_completed_rockets))
