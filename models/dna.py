import random
from pygame.math import *

from shared.configs import *


class Dna:
    """
    The genes representing the Agent
    """

    def __init__(self, genes=None):
        self.is_mutated = False
        self.genes = [self._get_random_vector() for _ in range(ROCKET_LIFESPAN)] \
            if genes is None else genes

    def crossover(self, other_dna):
        """ Recombination of two parent dna's to generate a new child dna """

        new_genes = []
        midpoint = int(random.random()*len(self.genes))
        new_genes += self.genes[:midpoint]
        new_genes += other_dna.genes[midpoint:]

        return Dna(genes=new_genes)

    def mutate(self):
        """ Maintain gene diversity by randomizing the genes based on a mutation probability """

        for i in range(len(self.genes)):
            if random.random() > MUTATION_PROBABILITY * 0.001:
                continue

            self.is_mutated = True
            mutated_gene = self._get_random_vector() * MUTATION_VARIATION
            self.genes[i] = mutated_gene

    def _get_random_vector(self):
        """ Return a randomized uniform vector in a random direction """

        return Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
