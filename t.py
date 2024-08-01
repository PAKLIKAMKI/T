import random
import numpy as np

# Function to choose multiplier
def choose_multiplier():
    # Define the range and probabilities
    multipliers = np.arange(1.1, 10.1, 0.1)
    probabilities = np.piecewise(multipliers, [multipliers <= 5, multipliers > 5], [0.9, 0.1])
    probabilities /= probabilities.sum()  # Normalize probabilities
    return np.random.choice(multipliers, p=probabilities)

# Function to choose a number between 1 and 10
def choose_number():
    numbers = np.arange(1, 11)
    probabilities = np.piecewise(numbers, [numbers <= 5, numbers > 5], [0.9, 0.1])
    probabilities /= probabilities.sum()  # Normalize probabilities
    return np.random.choice(numbers, p=probabilities)

# Example usage
multiplier = choose_multiplier()
number = choose_number()

print(f"Chosen Multiplier: {multiplier}")
print(f"Chosen Number: {number}")
