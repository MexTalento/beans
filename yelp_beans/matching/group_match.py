# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import random

from deap import algorithms
from deap import base
from deap import creator
from deap import tools


def generate_meetings(users, spec, group_size, prev_meeting_tuples=None, generations=10):
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()

    toolbox.register("attr_user", random.choice, users)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_user, n=group_size)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    def evalOneMax(individual):
        return 1,

    toolbox.register("evaluate", evalOneMax)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutUniformInt, low=0, up=group_size, indpb=0.05)

    def mutate_test(gene):
        gene[random.randint(0, len(gene) - 1)] = random.randint(0, 8)

    toolbox.register("select", tools.selTournament, tournsize=3)

    population = toolbox.population(n=50)

    for gen in range(generations):
        offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)
        fits = toolbox.map(toolbox.evaluate, offspring)
        for fit, ind in zip(fits, offspring):
            ind.fitness.values = fit
        population = toolbox.select(offspring, k=len(population))
    return tools.selBest(population, k=1)[0]
