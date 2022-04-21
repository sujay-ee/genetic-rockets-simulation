from pygame import Vector2

from shared.configs import *


class World:
    """
    The environment the agents interact with,
    Responsible for handling all environment related entities, in this case the obstacles, border collision etc
    """

    def __init__(self, visualizer):
        self.visualizer = visualizer
        self.target = Vector2(*TARGET_LOCATION)

        self.obstacles = []

    def draw(self):
        # Draw the target
        self.visualizer.draw_circle(TARGET_COLOR, self.target, TARGET_RADIUS)

        # Draw the obstacles
        for st, nd in self.obstacles:
            self.visualizer.draw_rect(OBSTACLE_COLOR, st, nd)

    def create_obstacle(self, start, end):
        self.obstacles.append((start, (end[0] - start[0], end[1] - start[1])))

    def check_world_collision(self, pos) -> bool:

        # A rocket at position (a, b) collides with screen borders of dimensions (w, h) when
        # a < 0 or a > w, or when b < 0 or b > h

        w, h = SCREEN_WIDTH, SCREEN_HEIGHT
        rocket_height = ROCKET_SIZE[1] / 2
        return pos.x <= 0+rocket_height or pos.x > w-rocket_height or \
               pos.y > h-rocket_height or pos.y <= 0+rocket_height

    def check_obstacles_collision(self, pos) -> bool:

        # A rocket at position (a, b) collides with a rectangle ((x1, y1), (x2, y2)) when
        # x1 < a < x2 and y1 < b < y2

        for st, nd in self.obstacles:
            if st[0] < pos.x < nd[0]+st[0] and \
                    st[1] < pos.y < nd[1]+st[1]:
                return True

        return False

    def check_target_collision(self, pos) -> bool:

        # A rocket at position (a, b) collides with a circle of radius r at (x, y) when
        # Distance from (a, b) to (x, y) <= r

        dist_to_target = pos.distance_to(self.target)
        return dist_to_target <= TARGET_RADIUS
