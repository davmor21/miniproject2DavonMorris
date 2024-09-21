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
import numpy as np
import pandas as pd
import requests

name = 'golden retriever'
api_url = 'https://api.api-ninjas.com/v1/dogs?name={}'.format(name)
response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)
