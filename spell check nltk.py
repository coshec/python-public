# importing the nltk suite
import nltk

# importing jaccard distance
# and ngrams from nltk.util
from nltk.metrics.distance import jaccard_distance
from nltk.util import ngrams
from nltk.corpus import words
  
  
correct_words = words.words()

# list of incorrect spellings
# that need to be corrected
incorrect_words=['happpy', 'azmaing', 'intelliengt']

# loop for finding correct spellings
# based on jaccard distance
# and printing the correct word
for word in incorrect_words:
 temp = [(jaccard_distance(set(ngrams(word, 2)),
        set(ngrams(w, 2))),w)
 for w in correct_words: 
  if w[0]==word[0]]:
   print(sorted(temp, key = lambda val:val[0])[0][1])

   ====

from textblob import TextBlob
TextBlob('A sentencee to checkk!').correct()
