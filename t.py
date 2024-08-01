import numpy as np
import requests

# Function to choose a multiplier between 1.1 and 10
def choose_multiplier():
    while True:
        multiplier = np.random.uniform(1.1, 10)
        if multiplier > 5:
            # Applying a lower probability for numbers over 5
            if np.random.random() < 0.1:  # 10% chance
                return multiplier
        else:
            return multiplier

# Function to choose a number between 1 and 10
def choose_number():
    while True:
        number = np.random.randint(1, 11)
        if number > 5:
            # Applying a lower probability for numbers over 5
            if np.random.random() < 0.1:  # 10% chance
                return number
        else:
            return number

# Example URL connection - note this is illustrative without specific API details
url = "https://lcg.bet/#/pages/venueGame/index"

# Function to simulate a post request
def send_data(url, data):
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Will raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Generate the values
multiplier = choose_multiplier()
number = choose_number()

# Prepare the data to send
data = {
    "multiplier": multiplier,
    "number": number
}

# Send the data
response = send_data(url, data)

# Output the result
print("Chosen Multiplier:", multiplier)
print("Chosen Number:", number)
print("Response from Server:", response)