Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import nltk
... from nltk.sentiment import SentimentIntensityAnalyzer
... 
... # Download VADER lexicon
... nltk.download('vader_lexicon')
... 
... # Initialize SentimentIntensityAnalyzer
... sia = SentimentIntensityAnalyzer()
... 
... # Function to analyze sentiment
... def analyze_sentiment(text):
...     sentiment_scores = sia.polarity_scores(text)
...     compound_score = sentiment_scores['compound']
...     
...     if compound_score >= 0.05:
...         sentiment = "Positive"
...     elif compound_score <= -0.05:
...         sentiment = "Negative"
...     else:
...         sentiment = "Neutral"
...     
...     return sentiment, sentiment_scores
... 
... # Example usage
... text = input("Enter a sentence: ")
... sentiment, scores = analyze_sentiment(text)
... 
... print(f"Sentiment: {sentiment}")
