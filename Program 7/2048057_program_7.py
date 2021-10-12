# -*- coding: utf-8 -*-
"""2048057_Program_7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zhkxQMBSPbY2hHabxUVvH8u5Zg_HiiG3

---
# <center> **NLP PROGRAM-7** </center>
## <center> A program for lemmatizing words using WordNet </center>
#### <center> Soundarya G_ 2048057</center>
---

* Try using a minimum of 10  different words, use the results, and based on that interpretations can be given. 
* Mention references such as papers as well for interpretation.
"""

# import these modules
import nltk
nltk.download('wordnet')

nltk.download('all')

!pip install simplemma

import simplemma

"""## Lemmatization

* In contrast to stemming, lemmatization is a lot more powerful. 

* It looks beyond word reduction and considers a language’s full vocabulary to apply a morphological analysis to words, aiming to remove inflectional endings only and to return the base or dictionary form of a word, which is known as the lemma.

* Lemmatization is the process of grouping together the different inflected forms of a word so they can be analyzed as a single item. Lemmatization is similar to stemming but it brings context to the words. So it links words with similar meanings to one word.

* Applications of lemmatization are:

      - Used in comprehensive retrieval systems like search engines.
      - Used in compact indexing

## Different Approaches on Lemmatization

### 1. Wordnet Lemmatizer

Wordnet is a publicly available lexical database of over 200 languages that provides semantic relationships between its words. It is one of the earliest and most commonly used lemmatizer technique.  

* It is present in the nltk library in python.
* Wordnet links words into semantic relations. ( eg. synonyms )
* It groups synonyms in the form of synsets.
"""

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

list_of_words = ['rocks','corpora','kites', 'babies', 'dogs', 'flying', 'smiling','driving', 'died', 'tried', 'feet']
for words in list_of_words:
	print(words + "\t : " + lemmatizer.lemmatize(words))

list_of_words_uppercase = ['FEET','CALFS','CHILDREN','WOMEN']
for words in list_of_words_uppercase:
	print(words + " : " + lemmatizer.lemmatize(words))

list_of_words_lowercase = ['feet','calfs','children','women']
for words in list_of_words_lowercase:
	print(words + " : " + lemmatizer.lemmatize(words))

list_of_words_suffix = ['sitting','seated','feeted','striped']
for words in list_of_words_suffix:
	print(words + " : " + lemmatizer.lemmatize(words))

"""* Non-English Languages"""

# TAMIL
list_of_words = ['பாறைகள்','காத்தாடி', 'நாய்கள்', 'புன்னகை', 'இறந்தார்']
for words in list_of_words:
	print(words + "\t : " + lemmatizer.lemmatize(words))

# GERMAN
list_of_words = ['Hier', 'Sind', 'Vaccines']
for words in list_of_words:
	print(words + " : " + lemmatizer.lemmatize(words))

"""> **Inference:**

        - The lemmas are same as the words since it isn't supporting non-english languages.
        - The lemmatization doesn't work properly, if the words are in uppercase.
        - If we notice the above words, the plural forms are converted to the singular form.
        - The general lemmatization, doesn't trunk the suffix 'ing','ed'.

* Simplemma
"""

# Simplemma supports diferent languages
mytokens = ['Hier', 'sein', 'Vaccines']
langdata = simplemma.load_data('de') # German
for token in mytokens:
  print(token + " : " +simplemma.lemmatize(token, langdata))

# Chaining Languages
langdata = simplemma.load_data('de', 'en')
simplemma.lemmatize('Vaccines', langdata)

"""> **Inference:**

      - sind means 'are' while sein means 'be'.
      - With its multilingual capacity, Simplemma can be configured to tackle several languages of interest.

### 2. Wordnet Lemmatizer with POS tag
"""

# a denotes adjective in "pos"
print("better :", lemmatizer.lemmatize("better"))
print("better :", lemmatizer.lemmatize("better", pos ="a"))

# v denotes verb in "pos"
print("cooking :", lemmatizer.lemmatize("cooking"))
print("cooking :", lemmatizer.lemmatize("cooking", pos ="v"))

print("playing :", lemmatizer.lemmatize("playing"))
print("playing :", lemmatizer.lemmatize("playing", pos ="v"))

print("dogs :", lemmatizer.lemmatize("dogs"))
print("dogs :", lemmatizer.lemmatize("dogs", pos ="n"))

print(lemmatizer.lemmatize("the cat is sitting with the bats on the striped mat under many badly flying geese"))

from nltk.corpus import wordnet

# Define function to lemmatize each word with its POS tag
def pos_tag(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:         
        return None

sentence = 'the cat is sitting with the bats on the striped mat under many badly flying geese'
 
# tokenize the sentence and find the POS tag for each token
pos_tagged = nltk.pos_tag(nltk.word_tokenize(sentence)) 
print(pos_tagged)

# we use our own pos_tagger function to make things simpler to understand.
wordnet_tagged = list(map(lambda x: (x[0], pos_tag(x[1])), pos_tagged))
print(wordnet_tagged)

"""> **Inference:**

      - The general sentence lemmatization without POS tagging doesn't trunk the word properly.
      - This is the sentence given for lemmatization "the cat is sitting with the bats on the striped mat under many badly flying geese", but we could see that the lemmatization using the POS tagging gave the exact content of the sentence.

References:
> https://www.geeksforgeeks.org/python-lemmatization-approaches-with-examples/

>https://www.machinelearningplus.com/nlp/lemmatization-examples-python/

>https://subscription.packtpub.com/book/application_development/9781782167853/2/ch02lvl1sec20/lemmatizing-words-with-wordnet
"""