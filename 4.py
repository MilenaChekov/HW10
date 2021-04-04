import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import t
import seaborn as sns

size = int(input())
rv = t(1)
v = []
for i in range(10000):
    s = np.mean(rv.rvs(size=size))
    v.append(s)
df = pd.DataFrame({'n': v})
df['PDF'] = rv.pdf(df['n'])
print(df)

a = sns.histplot(data=df, x='n', stat='density')
a = sns.lineplot(data=df, x='n', y='PDF')
plt.xlim(-3, 3)
plt.tight_layout()
a.figure.savefig(str(size)+'.png')