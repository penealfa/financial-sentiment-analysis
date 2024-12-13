import pandas as pd
import matplotlib.pyplot as plt

def publisher_date_analysis(df):
    length_counts = df.groupby('date')['headline'].count().reset_index()
    length_counts.columns = ['date', 'articles_count']
    top_20_publishers = length_counts.sort_values(by='articles_count', ascending=False).head(20)
    plt.figure(figsize=(15, 11))
    plt.barh(top_20_publishers['date'], top_20_publishers['articles_count'], color='skyblue')
    plt.title('Top Publication Dates')
    plt.xlabel('Number of Articles')
    plt.ylabel('date')
    plt.xticks(rotation=45)
    plt.show()

def weekday_publication_analysis(df):
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['weekday'] = df['date'].dt.day_name()
    weekday_counts = df.groupby('weekday')['headline'].count().reindex(
        ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    )
    plt.figure(figsize=(10, 6))
    weekday_counts.plot(kind='bar', color='skyblue')
    plt.title('Number of Articles Published by Weekday')
    plt.xlabel('Weekday')
    plt.ylabel('Number of Articles')
    plt.xticks(rotation=45)
    plt.show()

def day_of_month_publication_analysis(df):
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['day_of_month'] = df['date'].dt.day
    day_counts = df.groupby('day_of_month')['headline'].count()
    plt.figure(figsize=(10, 6))
    day_counts.plot(kind='bar', color='lightgreen')
    plt.title('Number of Articles Published by Day of Month')
    plt.xlabel('Day of Month')
    plt.ylabel('Number of Articles')
    plt.xticks(range(1, 32), rotation=45)
    plt.show()

def month_publication_analysis(df):
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['month'] = df['date'].dt.month_name()
    month_counts = df.groupby('month')['headline'].count().reindex(
        ['January', 'February', 'March', 'April', 'May', 'June', 
         'July', 'August', 'September', 'October', 'November', 'December']
    )
    plt.figure(figsize=(12, 6))
    month_counts.plot(kind='bar', color='coral')
    plt.title('Number of Articles Published by Month')
    plt.xlabel('Month')
    plt.ylabel('Number of Articles')
    plt.xticks(rotation=45)
    plt.show()

