import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_clipboard()
title = str(df.columns[0])
x = df[df.columns[0]]

plt.hist(x, bins=20)
plt.xlabel(title)
plt.ylabel('Frequency')
plt.title(title)
plt.savefig(f'hist/coffee_{title}_hist.png')
plt.clf()



