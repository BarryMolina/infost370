import pandas as pd
import subprocess
from scipy import stats

df = pd.read_clipboard()
x = df.iloc[:, 0]
(w, p) = stats.shapiro(x)
formatted = f'{w}\t{p}'
print(formatted)

subprocess.run("pbcopy", text=True, input=formatted)

