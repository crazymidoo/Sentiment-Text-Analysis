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

###AGGIUNGERE IF COSI MI DICE DIRETTAMENTE SE IL SENTIMENT = POSITIVO, NEGATIVO O NEUTRO E NON POLARITY 

blob = TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1
print("Sentiment Polarity: " + str(sentiment))

# -1.0 → molto negativo
# 0.0 → neutro
# +1.0 → molto positivo