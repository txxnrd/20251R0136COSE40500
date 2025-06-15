###### 20251R0136COSE405003 #######
# Title: Simple Sentiment Analyzer
# Description: This Python script implements a basic sentiment analyzer.
# It uses predefined positive and negative word lists to classify user input
# as positive, negative, or neutral sentiment. No machine learning is used.

positive_words = ["good", "great", "happy", "awesome", "fantastic", "love","brilliant","fabulous"]
negative_words = ["bad", "terrible", "sad", "horrible", "hate", "worst","awful"]

def analyze_sentiment(text):
    text = text.lower()  # Convert to lowercase for uniform comparison
    pos = sum(word in text for word in positive_words)
    neg = sum(word in text for word in negative_words)
    if pos > neg:
        return "Positive 😊"
    elif neg > pos:
        return "Negative 😠"
    else:
        return "Neutral 😐"
    
    
while True:
    user_input = input("Enter a sentence (type 'exit' to quit): ")
    if user_input == "exit":
        break
    print(analyze_sentiment(user_input))