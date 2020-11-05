import numpy as np
import pandas as pd
from datetime import date
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import sys 

# df = pd.read_csv('datasets/listings.csv')
# summary = df.dropna(subset=['summary'], axis=0)['summary']


def format_date(date):
  return f'{date.day}-{date.month}-{date.year}'

def build_wordcloud_with_mask(all_words, stopwords, mask):  
  wordcloud = WordCloud(
    stopwords=stopwords, 
    background_color='black', 
    width=1920, height=1080, 
    mask=mask
  ).generate(all_words)

  return wordcloud.to_file(f'{format_date(date.today())}.png')

def build_wordcloud_without_mask(all_words, stopwords):
   wordcloud = WordCloud(
    stopwords=stopwords, 
    background_color='black', 
    width=1920, height=1080 
  ).generate(all_words)

  return wordcloud.to_file(f'{format_date(date.today())}.png')


try:
  words_path = str(sys.argv[1])
  mask_path = str(sys.argv[2])

  
  if(words_path != None and not words_path.isspace()):
    try:
      words = open(words_path)

      all_words = " ".join(word for word in words)

      stopwords = set(STOPWORDS)
      stopwords.update(['da', 'meu', 'em', 'você', 'de', 'ao', 'os', 'que', 'ola', 'deseja'])

      if(mask_path != None and not mask_path.isspace()):
        mask = np.array(Image.open(mask_path))

        build_wordcloud_with_mask(all_words, stopwords, mask)
      else:
        build_wordcloud_without_mask(all_words, stopwords)

    except:
      print('Corrija os parâmetros e tente novamente')

except:
  print('error')