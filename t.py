import numpy as np
import requests

# Function to select a multiplier with a lower probability for numbers over 5
def select_multiplier():
    def weight(x):
        return 1 if x <= 5 else 0.1

    multipliers = np.arange(1.1, 10.1, 0.1)
    weights = np.array([weight(x) for x in multipliers])
    normalized_weights = weights / weights.sum()

    return np.random.choice(multipliers, p=normalized_weights)

# Function to select a number with a lower probability for numbers over 5
def select_number():
    def weight(x):
        return 1 if x <= 5 else 0.1

    numbers = np.arange(1, 11)
    weights = np.array([weight(x) for x in numbers])
    normalized_weights = weights / weights.sum()

    return np.random.choice(numbers, p=normalized_weights)

# Function to connect to the website
def connect_to_website():
    url = "https://lew.bet/#/pages/venueGame/index"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Successfully connected to the website.")
            return response.text
        else:
            print(f"Failed to connect to the website. Status code: {response.status_code}")
            return None
    except requests.ConnectionError as e:
        print(f"Connection error: {e}")
        return None

# Example usage
multiplier = select_multiplier()
number = select_number()

print(f"Selected multiplier: {multiplier}")
print(f"Selected number: {number}")

# Connect to the website
website_content = connect_to_website()
if website_content:
    # Process the content as needed
    print("Website content fetched successfully.")
