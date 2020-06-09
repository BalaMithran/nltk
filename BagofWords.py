import nltk

paragraph =  """Bag of Words (BOW) is a method to extract features from text documents.
These features can be used for training machine learning algorithms.
It creates a vocabulary of all the unique words occurring in all the documents in the training set.
In simple terms, it’s a collection of words to represent a sentence with word count and
mostly disregarding the order in which they appear."""
               
               
# using stopwords
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

ps = PorterStemmer()
wordnet=WordNetLemmatizer()
sentences = nltk.sent_tokenize(paragraph)
corpus = []
for i in range(len(sentences)):
    review = re.sub('[^a-zA-Z]', ' ', sentences[i])
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
    
# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
