# INF601 - Advanced Programming in Python
# Davon Morris
# Mini Project 2
import pandas as pd
import matplotlib.pyplot as plt
import requests
import os
import sys


if os.path.isfile('config.py'):
    from config import dogs_api_key
else:
    print("Config file not found. Stopping")
    sys.exit()
# Making charts directory if it doesn't exist
if not os.path.exists("charts/"):
    os.mkdir("charts/")

# List of dog names
dog_names = ['Golden Retriever', 'Doberman', 'Poodle', 'Dachshund', 'Husky']

# Initialize a list to store data for API Calls
dog_data = []

# Fetch data from the API for each dog
for dog in dog_names:
    api_url = 'https://api.api-ninjas.com/v1/dogs?name={}'.format(dog)
    response = requests.get(api_url, headers={'X-Api-Key': dogs_api_key})

    if response.status_code == requests.codes.ok:
        data = response.json()
        # Extract relevant traits
        traits = {
            'name': dog,
            'good_with_children': data[0]["good_with_children"],
            'good_with_other_dogs': data[0]["good_with_other_dogs"],
            'shedding': data[0]["shedding"],
            'drooling': data[0]["drooling"],
            'playfulness': data[0]["playfulness"]
        }
        dog_data.append(traits)
    else:
        print("Error:", response.status_code, response.text)

# Create a DataFrame from the collected data
df = pd.DataFrame(dog_data)

# Define x-axis labels
x_axis_labels = ['Good with Children', 'Good with Other Dogs', 'Shedding', 'Drooling', 'Playfulness']

# Loop through each row in the DataFrame to create plots
for index, row in df.iterrows():
    x_axis = [
        row["good_with_children"],
        row["good_with_other_dogs"],
        row["shedding"],
        row["drooling"],
        row["playfulness"]
    ]

    fig, ax = plt.subplots(figsize=(len(x_axis) * 2 + 2, 6))
    bar_container = ax.bar(x_axis_labels, x_axis, width=0.5)

    ax.set(ylabel='Trait Likelihood', ylim=(0, 5))
    ax.set_title(f"{row['name']} Breed's Traits", pad=20)

    ax.bar_label(bar_container, fmt='{:,.0f}', padding=10)
    ax.legend()

    #plt.show()
    try:
        plt.savefig(f"charts/{row['name']}_plot.png")
        print(f"{row['name']}_plot.png was created and has been saved to the 'charts' folder.")
    except:
        print(f"{row['name']}_plot.png failed to be created and/or was unable to be saved to the charts folder")