#RANDOM MODULE IN PYTHON
"""The random module in Python provides various functions for generating random numbers, 
selecting random elements, and shuffling sequences."""

#Let's see some of the important functions and methods from this module
import random

#random.random()
"""Returns a random float between 0.0 and 1.0."""
print(random.random())  # Example output: 0.8473

#random.uniform(a, b)
"""Returns a random float between a and b."""
print(random.uniform(5, 7.5))  # Example output: 3.27

#random.randint(a, b)
"""Returns a random integer between a and b (both inclusive)."""
print(random.randint(1, 10))  # Example output: 7

#random.randrange(start, stop, step)
"""Returns a random integer from range(start, stop, step)."""
print(random.randrange(1, 10, 2))  # Example output: 1,3, 5, 7, or 9

#random.choice(sequence)
"""Returns a random element from a non-empty sequence (list, tuple, string)."""
choices = ['apple', 'banana', 'cherry']
print(random.choice(choices))  # Example output: 'banana'

#random.choices(sequence, weights=None, k=1)
"""Returns k random elements with replacement (allows duplicates)."""
print(random.choices([1, 2, 3, 4], k=2))  # Example output: [3, 1]

#random.sample(sequence, k)
"""Returns k unique random elements without replacement."""
print(random.sample([1, 2, 3, 4, 5], 3))  # Example output: [2, 5, 1]

#random.shuffle(sequence)
"""Shuffles a list in-place."""
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)  # Example output: [3, 1, 5, 2, 4]

#random.seed(a)
"""Sets the seed for reproducible random results"""
random.seed(42)
print(random.randint(1, 100))  # Always gives the same result when the seed is set.