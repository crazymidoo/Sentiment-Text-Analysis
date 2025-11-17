## Sentiment Analysis From a Text (text.txt)

from textblob import TextBlob
from googletrans import Translator

with open('text.txt', 'r') as f:
    text = f.read()

translator = Translator()
translation = translator.translate(text, dest='en') # Traduzione tramite googletrans
eng = translation.text 

print("Translated:", eng)

# Sentiment in inglese
blob_eng = TextBlob(eng)
print("Sentiment (EN):", blob_eng.sentiment.polarity)

# -1.0 → molto negativo
# 0.0 → neutro
# +1.0 → molto positivo