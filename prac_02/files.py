out_file = open("name.txt", "w")

print("What is your name?")
name = str(input(">>> "))
out_file.write(name)

out_file.close()

in_file = open("name.txt", "r")

name_output = in_file.readline()
print("Your name is", name_output)

in_file.close()

out_file = open("numbers.txt", "r")

number1 = int(out_file.readline())
number2 = int(out_file.readline())

total_number = number1 + number2
print(total_number)
