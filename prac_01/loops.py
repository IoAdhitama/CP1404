print('1 : Display all of the odd numbers between 1 and 20')
print('2 : Count in 10s from 0 to 100')
print('3 : Count down from 20 to 1')
choice = int(input('Select loop to display: '))

if choice == 1:
    for i in range(1, 21, 2):
        print(i, end=' ')
    print()

elif choice == 2:
    for i in range(0, 110, 10):
        print(i, end=' ')
    print()

elif choice == 3:
    for i in range(20, 0, -1):
        print(i, end=' ')
    print()

else:
    print("invalid choice")