import numpy as np

# Function to generate a number between 1.1 and 10 with lower probability for numbers over 10
def choose_multiplier():
    while True:
        num = np.random.exponential(scale=1.5) + 1.1  # Adjust the scale to control the probability distribution
        if num <= 10:
            return num

# Function to generate a number between 1 and 10 with lower probability for numbers over 10
def choose_number():
    while True:
        num = np.random.exponential(scale=1.5) + 1  # Adjust the scale to control the probability distribution
        if num <= 10:
            return num

# Example usage
multiplier = choose_multiplier()
number = choose_number()

print(f"Chosen multiplier: {multiplier}")
print(f"Chosen number: {number}")
