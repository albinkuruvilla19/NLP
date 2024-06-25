import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Sample text
text = "Hello there! How are you doing today? This is a sample text for tokenization, stemming, lemmatization, and stopword removal."

# Sentence tokenization
sentences = sent_tokenize(text)
print("Sentences:")
for sentence in sentences:
    print(sentence)

# Word tokenization
words = word_tokenize(text)
print("\nWords:")
print(words)

# Stopword removal
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]
print("\nFiltered Words (Stopword Removal):")
print(filtered_words)

# Stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_words]
print("\nStemmed Words:")
print(stemmed_words)

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
print("\nLemmatized Words:")
print(lemmatized_words)
