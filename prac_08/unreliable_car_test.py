from prac_08.unreliable_car import UnreliableCar
import random


def main():
    reliability = random.uniform(0, 100)
    test_car = UnreliableCar("Test car", 100, reliability)
    print(test_car, "Reliability={}".format(reliability))
    test_car.drive(50)
    print(test_car)


main()
