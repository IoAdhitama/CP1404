from prac_06.guitar import Guitar

tester = Guitar("Gibson L-5 ECS", 1922, 16035.40)
tester2 = Guitar("Another Guitar", 1922, 5)
print(tester)
print("{} get_age() - Expected 96, got {}".format(tester.name, tester.get_age()))
print("{} get_age() - Expected 6, got {}".format(tester2.name, tester2.get_age()))

print("{} is_vintage() - Expected True, got {}".format(tester.name, tester.is_vintage()))
print("{} is_vintage() - Expected False, got {}".format(tester2.name, tester2.is_vintage()))

