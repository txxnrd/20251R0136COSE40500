###### 20251R0136COSE405003 #######
# Title: Simple Sentiment Analyzer
# Description: This Python script implements a basic sentiment analyzer.
# It uses predefined positive and negative word lists to classify user input
# as positive, negative, or neutral sentiment. No machine learning is used.
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    scores = analyzer.polarity_scores(text)
    if scores['compound'] >= 0.05:
        return "Positive 😊"
    elif scores['compound'] <= -0.05:
        return "Negative 😠"
    else:
        return "Neutral 😐"
    
    
while True:
    user_input = input("Enter a sentence (type 'exit' to quit): ")
    if user_input == "exit":
        break
    print(analyze_sentiment(user_input))