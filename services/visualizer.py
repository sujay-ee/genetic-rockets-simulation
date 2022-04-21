import sys
import pygame
from pygame.draw import circle
from pygame.draw import rect

from shared.configs import *


class Visualizer:
    """
    Responsible for visualization of the simulation,
    A wrapper around pygame library
    """

    def __init__(self):
        self.screen = None
        self.font = None
        self.is_paused = True
        self.mouse_points = []

        self.clock = pygame.time.Clock()
        self._init_pygame()

    def clock_tick(self):
        self.clock.tick(SIM_FPS)

    def get_events(self):
        for event in pygame.event.get():
            self._handle_events(event)

        # Draw mouse point hits
        for i in self.mouse_points:
            self.draw_circle(WHITE, i, 2)
            self.repaint()

        # Get obstacle points
        obstacle_points = None
        if len(self.mouse_points) == 2:
            obstacle_points = self.mouse_points
            self.mouse_points = []

        return self.is_paused, obstacle_points

    def show_text(self, pos, message):
        text_surface = self.font.render(message, True, SIM_STATS_FONT_COLOR)
        self.screen.blit(text_surface, dest=pos)

    def draw_mouse_point(self, pos):
        circle(self.screen, WHITE, pos, 2)
        self.repaint()

    def draw_circle(self, color, pos, radius):
        circle(self.screen, color, pos, radius)

    def draw_rect(self, color, start, end):
        rect(self.screen, color, pygame.Rect(*start, *end))

    def draw_surface(self, surface, pos):
        self.screen.blit(surface, pos)

    def _handle_events(self, event):
        if event.type == 256:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.is_paused = not self.is_paused
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # event.button == 1 => left mouse click
            self.mouse_points.append(event.pos)

    def _init_pygame(self):
        # Set up pygame components
        pygame.init()
        self.screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Rockets")
        self.font = pygame.font.Font(
            pygame.font.get_default_font(), SIM_STATS_FONT_SIZE)

        # Draw the window onto the screen
        pygame.display.update()

    def reset(self):
        self.screen.fill(SIM_BACKGROUND)

    @staticmethod
    def repaint():
        pygame.display.flip()
