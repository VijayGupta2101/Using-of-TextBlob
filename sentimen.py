from textblob import TextBlob
from textblob import Word

# Sample text
text = TextBlob("Virat Kohli is an amazing cricketer. I love his batting skills!")

# 1. Sentiment Analysis
print("1. Sentiment Analysis:")
print(text.sentiment)
print()

# 2. Tokenization
print("2. Tokenization:")
print("Words:", text.words)
print("Sentences:", text.sentences)
print()

# 3. Part-of-Speech Tagging
print("3. POS Tagging:")
print(text.tags)
print()

# 4. Noun Phrase Extraction
print("4. Noun Phrases:")
print(text.noun_phrases)
print()

# 5. Spelling Correction
print("5. Spelling Correction:")
wrong_text = TextBlob("I havv goood speling")
print("Original:", wrong_text)
print("Corrected:", wrong_text.correct())
print()

# 6. Translation
print("6. Translation:")
try:
    print(text.translate(to='hi'))
except Exception as e:
    print("Translation requires internet connection")
print()

# 7. Word Inflection (Singular/Plural)
print("7. Word Inflection:")
word = TextBlob("cars")
print("Singular:", word.words[0].singularize())
word2 = TextBlob("child")
print("Plural:", word2.words[0].pluralize())
print()

# 8. Lemmatization (basic using WordNet)
print("8. Lemmatization:")
w = Word("running")
print("Lemmatized:", w.lemmatize("v"))
print()

# 9. Word Count and Frequency
print("9. Word Frequency:")
for word, count in text.word_counts.items():
    print(word, ":", count)
print()

# 10. N-grams
print("10. N-grams (bigrams):")
print(text.ngrams(2))
print()

# 11. Language Detection (optional)
print("11. Language Detection:")
try:
    print(text.detect_language())
except:
    print("Language detection may not work without internet")