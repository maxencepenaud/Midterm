import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
Bigger50_numbers = ['XX' if num <= 50 else num for num in random_numbers]

# Print the processed list
print(Bigger50_numbers)


