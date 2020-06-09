import nltk
nltk.download()

paragraph = """The NLTK module is a massive tool kit,
aimed at helping you with the entire Natural Language Processing (NLP) methodology.
NLTK will aid you with everything from splitting sentences from paragraphs, splitting up words,
recognizing the part of speech of those words, highlighting the main subjects,
and then even with helping your machine to understand what the text is all about.
In this series,
we're going to tackle the field of opinion mining, or sentiment analysis."""
               
# Tokenizing sentences
sentences = nltk.sent_tokenize(paragraph)

# Tokenizing words
words = nltk.word_tokenize(paragraph)
