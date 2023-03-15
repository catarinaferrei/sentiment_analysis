import json
import numpy as np

# Read input JSON file
with open('output_file_app.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extract sentiment scores for each tweet
# Extract sentiment scores for each tweet
negative_scores = []
neutral_scores = []
positive_scores = []

for tweet in data:
    sentiment_scores = tweet['sentiment_scores']
    negative_scores.append(sentiment_scores['negative'])
    neutral_scores.append(sentiment_scores['neutral'])
    positive_scores.append(sentiment_scores['positive'])

# Compute statistics on sentiment scores
avg_negative_score = np.mean(negative_scores)
avg_neutral_score = np.mean(neutral_scores)
avg_positive_score = np.mean(positive_scores)
std_negative_score = np.std(negative_scores)
std_neutral_score = np.std(neutral_scores)
std_positive_score = np.std(positive_scores)

# Print results
print(f"Negative scores: avg={avg_negative_score:.4f}, std={std_negative_score:.4f}")
print(f"Neutral scores: avg={avg_neutral_score:.4f}, std={std_neutral_score:.4f}")
print(f"Positive scores: avg={avg_positive_score:.4f}, std={std_positive_score:.4f}")