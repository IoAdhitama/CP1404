"""
Program to quickly work out the total price
for a number of items, each with different
prices.
"""

def main():
    # Getting amount of items
    item_amount = int(input("Number of items: "))
    while item_amount < 0:
        print("Invalid number of items!")
        item_amount = int(input("Number of items: "))

    # Getting price of each item, and adding it to total price
    total_price = 0
    for i in range(0, item_amount, 1):
        item_price = float(input("Price of item: "))
        total_price = total_price + item_price

    # Discount calculation (if total price above 100)
    if total_price > 100:
        total_price = 0.9 * total_price

    # Displaying the result
    print("Total price for {} items is ${:.2f}".format(item_amount, total_price))

main()