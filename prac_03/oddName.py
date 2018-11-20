def main():
    name = get_name()

    name_print(name)


def name_print(name):
    for i in range(0, len(name), 2):
        print(name[i])


def get_name():
    name = str(input("Enter a name: "))
    return name


main()