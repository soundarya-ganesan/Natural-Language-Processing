# -*- coding: utf-8 -*-
"""2048057_Program_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V2cp0z1xGDGyAqg9lMLcoo8iujoooigJ

---
# <center> **NLP PROGRAM-3** </center>
## <center> A program to tokenize Non-English Languages </center>
#### <center> Soundarya G_ 2048057</center>
---

## Different Indian Language Texts used for the Program

> *   Tamil_text = '''வணக்கம் எப்படி இருக்கிறாய்'''
*   Hindi_text = '''नमस्ते कैसी हो तुम'''
*   Punjabi_text = '''ਹੈਲੋ ਤੁਸੀ ਕਿਵੇਂ ਹੋ'''
*   Telugu_text = '''సంస్కృతానికి'''
*   Gujarati_text = '''હેલો કેમ છો?'''
*   Kannada_text = '''ನಮಸ್ಕಾರ ಹೇಗಿದ್ದೀರಾ'''
*   Malayalam_text = '''ഹലോ, നിങ്ങൾക്ക് സുഖമാണോ'''
*   Nepali_text = '''नमस्ते तपाइँ कसरी हुनुहुन्छ?'''
*   Odia_text = '''ହେ ତମେ କେମିତି ଅଛ'''
*   Marathi_text = '''नमस्कार तुम्ही कसे आहात'''
*   Bengali_text = '''হ্যালো, আপনি কেমন আছেন'''
*   Urdu_text = '''ہیلو آپ کیسے ہیں'''

## Import necessary libraries
"""

# pip install inltk
# pip install langdetect
# pip install googletrans

from inltk.inltk import setup
from inltk.inltk import tokenize
from langdetect import detect
import pandas as pd

"""# Different Indian Languages for tokenization"""

indian_languages={'hi': 'Hindi','pa': 'Punjabi','te': 'Telugu','gu': 'Gujarati',
                  'kn': 'Kannada','ml': 'Malayalam','ne': 'Nepali','or': 'Odia',
                  'mr': 'Marathi','bn': 'Bengali','ta': 'Tamil','ur': 'Urdu'} 

df = pd.DataFrame(list(indian_languages.items()),columns = ['Code','Language'])
df

"""# User Text Function

This function takes input from user for the tokenization.
"""

def user_text_func():
  text = input('\t')
  return text

user_text = user_text_func()

"""# Language Detector

Detects which language is given as text.
"""

print(detect(user_text), '-',indian_languages[detect(user_text)])

"""# Setup for the user text's language"""

def setup_for_lang(text):
  try:
    setup(detect(text))
  except RuntimeError:
    #print('language setup is successful')
    return detect(text)
  else:
    print('error')

Lang = setup_for_lang(user_text)
Lang

"""# Language Translator"""

# User input translated to English
from googletrans import Translator
translator = Translator()
translator.translate('வணக்கம்',src='ta',dest='en')

"""# Tokenization """

# tokenize(input text, language code)
tokenize(user_text,Lang)

Lang_token_list = tokenize(user_text,Lang)
check = '▁'
token_list = [idx for idx in Lang_token_list if idx[0]==check]
token_list

new_token_list = [s.replace('▁','') for s in token_list]
new_token_list

"""# Main Function"""

def Non_English_Language_Translator():
  indian_languages={'hi': 'Hindi','pa': 'Punjabi','te': 'Telugu','gu': 'Gujarati',
                  'kn': 'Kannada','ml': 'Malayalam','ne': 'Nepali','or': 'Odia',
                  'mr': 'Marathi','bn': 'Bengali','ta': 'Tamil','ur': 'Urdu'} 

  df = pd.DataFrame(list(indian_languages.items()),columns = ['Language','Code'])
  print(df)
  option = 'yes'
  while(option == 'yes'):
    print('\nType your text to be tokenized')
    user_text = user_text_func()
    Lang = setup_for_lang(user_text)
    Lang_token_list = tokenize(user_text,Lang)
    check = '▁'
    token_list = [idx for idx in Lang_token_list if idx[0]==check]
    new_token_list = [s.replace('▁','') for s in token_list]
    print('\n\tUser Input \t\t :', user_text)
    print('\tLanguage Identified \t :', indian_languages[Lang])
    print('\tLanguage Code \t\t :', Lang)
    print('\tTokens \t\t\t :', new_token_list)
    print('\tNo. of Tokens \t\t :', len(new_token_list), 'Tokens')
    print('\tEnglish Translation \t : On progress!!!')

    print('\n\t\tDo you want to continue the program')
    option = input('\t\t\t[yes/no]:')

Non_English_Language_Translator()