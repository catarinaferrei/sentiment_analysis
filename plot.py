import json
import pandas as pd
import matplotlib.pyplot as plt

# Read input JSON file
# Read input JSON file
with open('output_file_app.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Load the data in a dataframe
df = pd.DataFrame(data)
pd.set_option('display.max_colwidth', None)

# Calculate the mean sentiment score for each sentiment
sentiment_means = df['sentiment_scores'].apply(lambda x: pd.Series(x)).mean()

# Visualize the sentiments with a pie chart
fig = plt.figure(figsize=(6,6), dpi=100)
ax = plt.subplot(111)
sentiment_means.plot.pie(ax=ax, autopct='%1.1f%%', startangle=270, fontsize=12, label="")
ax.set_title('Sentiment Analysis', fontsize=16)
plt.show()
