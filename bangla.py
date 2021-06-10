from os import path
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
from bnlp.corpus import stopwords


file = open("Dataset/banglaText.txt", "r", encoding='UTF-8')
text = file.read()
#print(text)


# create numpy araay for wordcloud mask image

mask = np.array(Image.open(path.join("cloud.png")))

# create set of stopwords
stopwords = set(stopwords())

#custome unicode
rgx = r"[\u0980-\u09FF]+"


#create wordcloud object
wc = WordCloud(background_color="white",
                   mask=mask,
                   stopwords = stopwords,
                   font_path="font/balooda.ttf",
                   regexp=rgx
               )

# generate wordcloud
wc.generate(text)


# save to wordcloud image
result = wc.to_file(path.join("wordCloudBangla.png"))