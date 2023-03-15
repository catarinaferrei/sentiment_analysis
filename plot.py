import json
import pandas as pd
import matplotlib.pyplot as plt

# Read input JSON file
with open('output_file_app.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Load the data in a dataframe
df = pd.DataFrame(data)
pd.set_option('display.max_colwidth', None)

# Extract sentiment with the highest score and create a new "sentiment" column
df['sentiment'] = df['sentiment_scores'].apply(lambda x: max(x, key=x.get))

# Show a tweet for each sentiment
print(df[df["sentiment"] == 'negative'].head(1))
print(df[df["sentiment"] == 'neutral'].head(1))
print(df[df["sentiment"] == 'positive'].head(1))

# Count the number of tweets by sentiments
sentiment_counts = df.groupby(['sentiment']).size()
print(sentiment_counts)

# Visualize the sentiments with a pie chart
fig = plt.figure(figsize=(6,6), dpi=100)
ax = plt.subplot(111)
sentiment_counts.plot.pie(ax=ax, autopct='%1.1f%%', startangle=270, fontsize=12, label="")
ax.set_title('Sentiment Analysis', fontsize=16)
plt.show()
