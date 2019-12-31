import random as rand
import utilities

class Node(object):
    """A basic node for the web."""

    def __init__(self):
        self.x = rand.uniform(-10, 10)
        self.y = rand.uniform(-10, 10)
        self.type = utilities.getRandDice()
        self.face = utilities.getRandDiceFace(self.type)
        self.depth = rand.uniform(-10, 0)
        self.neighbors = []
