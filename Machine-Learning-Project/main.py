from textblob import TextBlob
from newspaper import Article

url = 'https://it.wikipedia.org/wiki/Matematica'
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.text
print(text)