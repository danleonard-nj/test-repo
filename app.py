import pandas as pd

data =  {
            'numbers'  : [1, 2, 3]
        }

df = pd.DataFrame.from_dict(data)

print(df)