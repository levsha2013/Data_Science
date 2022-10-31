import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('iris.data', header=None)
print(df.head())

main = {name: color for name, color in zip(set(df[4]), ['r', 'g', 'blue'])}
colors = [main[df.iloc[i, 4]]for i in range(df.shape[0])]

df['colors'] = pd.Series(colors)
plt.scatter(df[0], df[1], alpha=0.2, c=df['colors'], s=100*df[3], cmap='viridis')
plt.show()
print()