import random

from models.rocket import Rocket
from shared.configs import *


class Population:

    """
    Service to handle creation and deletion of test agents, rockets in this case
    """

    def __init__(self, visualizer, world):
        self.visualizer = visualizer
        self.world = world

        # Setup 1st generation of rockets
        self.rockets = [Rocket(self.visualizer) for _ in range(NUM_ROCKETS)]

    def update(self, frame_count):
        [r.update(frame_count, self.world) for r in self.rockets]

    def draw(self):
        [r.draw() for r in self.rockets]

    def start_new_generation(self, best_fitness):

        # Normalize the fitness of the rockets
        [r.normalize_fitness(best_fitness) for r in self.rockets]

        # Create a gene pool for Roulette Wheel Selection
        gene_pool = []
        for i, r in enumerate(self.rockets):
            gene_probability = int(r.fitness * 100)
            gene_pool += [i] * gene_probability

        new_rockets = []
        for i in range(NUM_ROCKETS):

            # Select parents from pool
            first_parent = self.rockets[random.choice(gene_pool)].dna
            second_parent = self.rockets[random.choice(gene_pool)].dna

            # Create a child dna with crossover
            child_dna = first_parent.crossover(second_parent)
            child_dna.mutate()
            new_rockets.append(Rocket(self.visualizer, child_dna))

        self.rockets = new_rockets

    def end_current_generation(self):

        # Calculate maximum fitness
        max_fitness = 0
        for r in self.rockets:
            r.calc_fitness()
            max_fitness = r.fitness \
                if r.fitness > max_fitness else max_fitness

        # Calculate number of completed rockets
        num_completed_rockets = sum(r.is_complete for r in self.rockets)

        return max_fitness, num_completed_rockets
