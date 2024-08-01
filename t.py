import numpy as np
import requests

# Function to choose a multiplier between 1.1 and 10 with a lower probability for numbers over 5
def choose_multiplier():
    while True:
        multiplier = np.random.uniform(1.1, 10)
        if multiplier > 5:
            if np.random.random() < 0.1:  # 10% chance for numbers over 5
                return multiplier
        else:
            return multiplier

# Function to choose a number between 1 and 10 with a lower probability for numbers over 5
def choose_number():
    while True:
        number = np.random.randint(1, 11)
        if number > 5:
            if np.random.random() < 0.1:  # 10% chance for numbers over 5
                return number
        else:
            return number

# Function to send data to the given URL with an API key
def send_data(url, data, api_key):
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Will raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Example URL - replace with the actual API endpoint if different
url = "https://lcg.bet/#/pages/venueGame/index"
api_key = "1LTHvAkbazj6y7B2AWUe-0"

# Generate the values
multiplier = choose_multiplier()
number = choose_number()

# Prepare the data to send
data = {
    "multiplier": multiplier,
    "number": number
}

# Send the data
response = send_data(url, data, api_key)

# Output the result
print("Chosen Multiplier:", multiplier)
print("Chosen Number:", number)
print("Response from Server:", response)
