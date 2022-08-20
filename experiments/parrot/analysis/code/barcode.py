# coding: utf-8
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df = pd.read_csv('experiments/parrot/results/22:17:48.tsv',sep='\t')
df = df.T.reset_index(drop=True).T
sns.heatmap(df,cmap='binary')
#sns.clustermap(df.fillna(0),cmap='binary')
#plt.show()
plt.savefig('../results/plot.png')
