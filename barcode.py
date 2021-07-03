# coding: utf-8
import pandas as pd
import seaborn as sns
df = pd.read_csv('experiments/parrot/results/22:17:48.tsv',sep='\t')
df
df = pd.read_csv('experiments/parrot/results/22:17:48.tsv')
df = pd.read_csv('experiments/parrot/results/22:17:48.tsv',sep='\t')
df
sns.heatmap(df)
df = pd.read_csv('experiments/parrot/results/22:17:48.tsv',sep='\t')
sns.heatmap(df)
import matplotlib.pyplot as plt
plt.show()
df = pd.read_csv('experiments/parrot/results/22:17:48.tsv',sep='\t',columns=[0,1,2,3,4,5,6,7,8,9])
df = pd.read_csv('experiments/parrot/results/22:17:48.tsv',sep='\t')
df = df.T.reset_index(drop=True).T
df
sns.boxplot(df)
sns.clustermap(df)
sns.heatmap(df)
plt.show()
sns.heatmap(df)
plt.show()
sns.heatmap(df,cmap='binary')
plt.show()
get_ipython().run_line_magic('save', 'barcode.py 1-25')
