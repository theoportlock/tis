# coding: utf-8
import matplotlib.pyplot as plt
import glob
import pandas as pd
import seaborn as sns

results = glob.glob('../results/*.tsv')
for result in results:
    try:
        df = pd.read_csv(result, sep='\t')
        df = df.T.reset_index(drop=True).T
        sns.heatmap(df,cmap='binary')
        #sns.clustermap(df.fillna(0),cmap='binary')
        #plt.show()
        #plt.savefig(f'../results/{result}.png')
        plt.show()
    except:
        None
