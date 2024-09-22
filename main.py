import sys

# df = pd.DataFrame(
#     {
#         "Name": [
#             "Braund, Mr. Owen Harris",
#             "Allen, Mr. William Henry",
#             "Bonnell, Miss. Elizabeth",
#         ],
#         "Age": [22, 35, 58],
#         "Sex": ["male", "male", "female"],
#     }
# )
#
# level = pd.Series(['sophmore', 'freshman', 'senior'], name = 'Student Level')
#
#
# print(level)
# #print(list(df.columns))
# #print(df['Age'])
# INF601 - Advanced Programming in Python
# Davon Morris
# Mini Project 2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from matplotlib.pyplot import ylabel
import requests
import os


if os.path.isfile('config.py'):
    from config import dogs_api_key
else:
    print("Config file not found. Stopping")
    sys.exit()


name = 'Golden Retriever'
api_url = 'https://api.api-ninjas.com/v1/dogs?name={}'.format(name)
response = requests.get(api_url, headers={'X-Api-Key': dogs_api_key})
if response.status_code == requests.codes.ok:
    print(response.text)
    data = response.json()
    #print(data)
    x_axis_labels = ('Good with Children', 'Good With Other Dogs', 'Shedding', "Drool", "Playfulness")
    x_axis = [(data[0]["good_with_children"]),(data[0]["good_with_other_dogs"]),(data[0]["shedding"]),(data[0]["drooling"]),(data[0]["playfulness"])]

    fig, ax = plt.subplots(figsize=((len(x_axis) * 2 + 2),6))
    bar_container = ax.bar(x_axis_labels, x_axis, width=.5)
    ax.set(ylabel='Trait Likelihood',ylim=(1,5))
    ax.set_title(f"{name} Breed's Traits", pad=20 )
    ax.bar_label(bar_container,fmt='{:,.0f}')
    ax.legend()
    plt.show()
else:
    print("Error:", response.status_code, response.text)
