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
    
print("Simple Sentiment Analyzer")
print("Type a sentence to analyze its sentiment.")
print("Type 'exit' to quit.\n")
while True:
    user_input = input("Enter a sentence (type 'exit' to quit): ")
    if user_input.lower() == "exit" == "exit":
        break
    if not user_input:
        print("Empty input. Please enter a sentence.")
        continue
    print(analyze_sentiment(user_input))
    result = analyze_sentiment(user_input)
    print(f"{result} | Score: {analyzer.polarity_scores(user_input)['compound']}")
