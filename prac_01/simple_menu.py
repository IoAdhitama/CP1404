def main():
    # Get name, initialize choice
    user_name = str(input("Enter name: "))

    # Display menu
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    print()
    # Get choice
    choice = str(input(">>> ").upper())

    while choice != 'Q':
        if choice == "H":
            print("Hello",user_name)
        elif choice == "G":
            print("Goodbye",user_name)
        else:
            print("Invalid choice")

        # Display menu
        print("(H)ello")
        print("(G)oodbye")
        print("(Q)uit")
        print()
        # Get choice
        choice = str(input(">>> ").upper())

    # Display finished message
    print("Finished.")


main()