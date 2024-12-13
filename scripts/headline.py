import pandas as pd
import matplotlib.pyplot as plt


def  headline_lenght_analysis(df):
    df['length'] = df['headline'].str.len()
    bins = list(range(0, 600, 50))
    labels = [f"{bins[i]}-{bins[i+1]}" for i in range(len(bins) - 1)]  
    df['length_class'] = pd.cut(df['length'], bins=bins, labels=labels, right=False)
    length_counts = df['length_class'].value_counts(sort=False)  
    plt.figure(figsize=(10, 6))
    length_counts.plot.bar(color='skyblue')
    plt.title('Distribution of Headline Lengths')
    plt.xlabel('Length Ranges')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

