import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

paragraph = """"""
               In linguistic morphology and information retrieval,
               stemming is the process of reducing inflected (or sometimes derived) words to their word stem,
               base or root form—generally a written word form. The stem need not be identical to the morphological root of the word;
               it is usually sufficient that related words map to the same stem, even if this stem is not in itself a valid root.
               
               
               Algorithms for stemming have been studied in computer science since the 1960s.
               Many search engines treat words with the same stem as synonyms as a kind of query expansion,
               a process called conflation.

               A computer program or subroutine that stems word may be called a stemming program, stemming algorithm,
               or stemmer"""
               
sentences = nltk.sent_tokenize(paragraph)
stemmer = PorterStemmer()

# Stemming
for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i] = ' '.join(words)
