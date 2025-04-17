import random

first_names = ["Alex", "Jamie", "Taylor", "Jordan", "Casey", "Riley", "Morgan", "Avery"]
last_names = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Thomas", "Jackson", "White"]

def generate_random_name():
    first = random.choice(first_names)
    last = random.choice(last_names)
    return f"{first} {last}"

# Generate 5 random names
for _ in range(5):
    print(generate_random_name())