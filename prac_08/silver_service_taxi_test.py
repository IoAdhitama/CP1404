from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Hummer", 200, 2)
    print(taxi)
    taxi.drive(18)
    print(taxi.get_fare())


main()
