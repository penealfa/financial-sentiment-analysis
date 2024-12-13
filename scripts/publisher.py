import pandas as pd
import matplotlib.pyplot as plt

def publisher_analysis(df):
    length_counts = df.groupby('publisher')['headline'].count().reset_index()
    length_counts.columns = ['publisher', 'articles_count']
    top_20_publishers = length_counts.sort_values(by='articles_count', ascending=False).head(20)
    plt.figure(figsize=(15, 11))
    plt.barh(top_20_publishers['publisher'], top_20_publishers['articles_count'], color='skyblue')
    plt.title('Number of Articles Published by Each Publisher')
    plt.xlabel('Number of Articles')
    plt.ylabel('Publisher')
    plt.xticks(rotation=45)
    plt.show()
