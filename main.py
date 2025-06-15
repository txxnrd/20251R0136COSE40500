###### 20251R0136COSE405003 #######
# Title: Simple Sentiment Analyzer
# Description: This Python script implements a basic sentiment analyzer.
# It uses predefined positive and negative word lists to classify user input
# as positive, negative, or neutral sentiment. No machine learning is used.
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from colorama import Fore, Style, init
init()

analyzer = SentimentIntensityAnalyzer()

def print_colored_result(result, score):
    if "Positive" in result:
        print(Fore.GREEN + f"{result} | Score: {score:.2f}" + Style.RESET_ALL)
    elif "Negative" in result:
        print(Fore.RED + f"{result} | Score: {score:.2f}" + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + f"{result} | Score: {score:.2f}" + Style.RESET_ALL)
        
def analyze_sentiment(text: str) -> str:
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
    if user_input.lower() == "exit":
        break
    if not user_input:
        print("Empty input. Please enter a sentence.")
        continue
    score = analyzer.polarity_scores(user_input)['compound']
    result = analyze_sentiment(user_input)
    print_colored_result(result, score)

def test_analyze_sentiment():
    assert analyze_sentiment("I love it!") == "Positive 😊"
    assert analyze_sentiment("This is awful.") == "Negative 😠"
    assert analyze_sentiment("I went to the store.") == "Neutral 😐"