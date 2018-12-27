import pandas as pd
import numpy as np

data = pd.read_csv('data.csv')

x = np.array(data[['x1', 'x2']])
y = np.array(data['y'])

print(data.head())

print(x)
print(y)
