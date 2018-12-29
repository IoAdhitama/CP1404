from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


MENU = """q)uit, c)hoose taxi, d)rive
>>> """


def main():
    user_input = ""
    taxi_used = 0
    current_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's Drive!")
    while user_input != "q":
        user_input = str(input(MENU)).lower()

        if user_input == "c":
            print("Taxis available:")
            for i in range(len(taxis)):
                print("{} - {}".format(i, taxis[i]))

            try:
                taxi_used = int(input("Choose taxi: "))
                taxis[taxi_used].start_fare()
            except ValueError:
                print("Invalid input.")

        if user_input == "d":
            try:
                distance = int(input("Drive how far? "))
                taxis[taxi_used].drive(distance)
                print("Your {} trip cost you ${}".format(taxis[taxi_used].name, taxis[taxi_used].get_fare()))
                current_bill += taxis[taxi_used].get_fare()
            except ValueError:
                print("Invalid input.")

        print("Bill to date: ${}".format(current_bill))

    print("Total trip cost: ${}".format(current_bill))
    print("Taxis are now:")
    for i in range(len(taxis)):
        print("{} - {}".format(i, taxis[i]))


main()
