TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


def main():
    print("Electricity bill estimator 2.0")
    print()

    tariff_type = int(input("Which tariff? 11 or 31: "))
    if tariff_type == 11 or tariff_type == 31:
        valid_input = True
        while not valid_input:
            print("Invalid input.")
            tariff_type = int(input("Which tariff? 11 or 31: "))
            if tariff_type == 11 or tariff_type == 31:
                valid_input = True

    daily_kwh_use = float(input("Enter daily use in kWh: "))
    while daily_kwh_use < 0:
        print("Invalid input.")
        daily_kwh_use = float(input("Enter daily use in kWh: "))

    billing_period = int(input("Enter number of billing days: "))
    while billing_period < 0:
        print("Invalid input.")
        billing_period = int(input("Enter number of billing days: "))

    if tariff_type == 11:
        estimate_bill = TARIFF_11 * daily_kwh_use * billing_period
    else:
        estimate_bill = TARIFF_31 * daily_kwh_use * billing_period

    print("Estimated bill: ${:.2f}".format(estimate_bill))


main()
