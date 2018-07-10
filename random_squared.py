import random


random_numbers = []
for x in range(0, 20):
    random_numbers.append(random.randint(0, 49))

print(random_numbers)


random_squared = [number**2 for number in random_numbers]

print(random_squared)