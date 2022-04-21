from shared.colors import *

# Simulation Configurations

# Window Dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 720

# Simulation Configs
NUM_ROCKETS = 500
SIM_BACKGROUND = DARK_BLUE
SIM_FPS = 120

# Visualizer configs
SIM_STATS_FONT_SIZE = 18
SIM_STATS_FONT_COLOR = WHITE
SIM_STATS_POSITION = (SCREEN_WIDTH - 145, SCREEN_HEIGHT - 75)

# Target Configs
TARGET_LOCATION = (SCREEN_WIDTH / 2, 50)
TARGET_COLOR = LIGHT_BLUE
TARGET_RADIUS = 15

# Obstacle Configs
OBSTACLE_COLOR = LIGHT_BLUE

# Rocket Configs
ROCKET_LIFESPAN = 250
ROCKETS_SPAWN_LOC = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 30)
ROCKET_SIZE = (5, 20)
ROCKET_COLOR = (*GREEN, 200)
ROCKET_COLOR_CRASHED = (*LIME, 150)
ROCKET_COLOR_COMPLETED = (*RED, 150)
ROCKET_COLOR_MUTATED = ROCKET_COLOR

# Mutation Configs
MUTATION_PROBABILITY = 5
MUTATION_VARIATION = 0.5
