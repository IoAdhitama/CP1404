from prac_06.guitar import Guitar


def main():
    guitars = []
    name = "Init"
    print("My Guitars!")
    while name != "":
        name = str(input("Name: "))
        if name == "":
            print("     ... snip ...")
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print("{} ({}) : ${} added.".format(name, year, cost))

    print("These are my guitars:")
    for i in range(len(guitars)):
        print("Guitar {}: {} ({}), worth ${}".format(i+1, guitars[i].name, guitars[i].year,
                                                        guitars[i].cost), end=" ")
        if guitars[i].is_vintage():
            print("(Vintage)")
        else:
            print()


main()
