import pygame
import random


class Food:
    def __init__(self, display):
        self.color = [(0, 255, 0), (0, 0, 255), (100,100, 100)]
        self.food = None
        self.generateFood(display)

    def draw(self, display):
        pygame.draw.rect(self.food[0], self.food[1], self.food[2])

    def generateFood(self, display):
        while True:
            tempX = random.randrange(1, 536)
            if tempX % 24 == 0:
                break
        while True:
            tempY = random.randrange(1, 536)
            if tempY % 24 == 0:
                break
        self.food = (display, random.choice(self.color), [tempX + 1, tempY + 1, 23, 23])




