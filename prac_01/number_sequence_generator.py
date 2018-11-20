def main():
    print("Number sequence generator")
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))

    print("(1) Show the even numbers from x to y")
    print("(2) Show the odd numbers from x to y")
    print("(3) Show the squares from x to y")
    print("(4) Exit the program")
    print()
    choice = str(input(">>> "))

    while choice != "4":
        if choice == "1":
            for i in range(x, y+1, 1):
                if i % 2 == 0:
                    print(i, end=' ')
            print()
        elif choice == "2":
            for i in range(x, y+1, 1):
                if i % 2 == 1:
                    print(i, end=' ')
            print()
        elif choice == "3":
            for i in range(x, y+1, 1):
                print(i ** 2, end=' ')
            print()
        else:
            print("invalid Choice")

        print("(1) Show the even numbers from x to y")
        print("(2) Show the odd numbers from x to y")
        print("(3) Show the squares from x to y")
        print("(4) Exit the program")
        print()
        choice = str(input(">>> "))


main()
