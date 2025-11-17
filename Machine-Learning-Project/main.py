## Sentiment Analysis From Link
from textblob import TextBlob
from newspaper import Article

url = 'https://www.milanotoday.it/video/video-esercitazione-passante-novembre-2025.html'
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1
print("Sentiment Polarity: " + str(sentiment))

# -1.0 → molto negativo
# 0.0 → neutro
# +1.0 → molto positivo