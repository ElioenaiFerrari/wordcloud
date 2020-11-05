import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import sys 

# df = pd.read_csv('datasets/listings.csv')
# summary = df.dropna(subset=['summary'], axis=0)['summary']

words = open(str(sys.argv[1]))

all_words = " ".join(word for word in words)

print(f'Quantidade de palavras {len(all_words)}')

stopwords = set(STOPWORDS)
stopwords.update(['da', 'meu', 'em', 'você', 'de', 'ao', 'os', 'que', 'ola', 'deseja'])

mask = np.array(Image.open(str(sys.argv[2])))

wordcloud = WordCloud(stopwords=stopwords, background_color='white', width=1920, height=1080, mask=mask).generate(all_words)

wordcloud.to_file('wordcloud.png')