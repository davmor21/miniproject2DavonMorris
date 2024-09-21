import numpy as np
import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

level = pd.Series(['sophmore', 'freshman', 'senior'], name = 'Student Level')


print(level)
#print(list(df.columns))
#print(df['Age'])
