"""
CP1404 Practical week 8
Unreliable car class
"""
from prac_08.car import Car
import random


class UnreliableCar(Car):
    """What an unreliable car!"""

    def __init__(self, name, fuel, reliability):

        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Sometimes the car will drive, sometimes it will not."""
        if random.randint(0, 100) <= self.reliability:
            super().drive(distance)
        else:
            print("The unreliable car won't drive. How unreliable!")
