
import datetime
import os
import telepot
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from datetime import date, timedelta
from google_play_scraper import app
from google_play_scraper import Sort, reviews_all, app, reviews
# from spacy.lang.en import English
from wordcloud import WordCloud, STOPWORDS
from google_trans_new import google_translator
from os import path
from PIL import Image
import time

all_reviews = reviews_all(
    'xyz.sheba.managerapp',
    sleep_milliseconds=0, # defaults to 0
    #lang='en', # defaults to 'en'
    #country='us', # defaults to 'us'
    #sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    #filter_score_with=5 # defaults to None(means all score)
)

df = pd.DataFrame(all_reviews)
df = df.rename(columns={'content':'ReviewText', 'score': 'Rating', 'at': 'TimeSTAMP', 'replyContent': 'DQMResponse', 'repliedAt':'DQMResponse_TimeStamp'})
df = df.drop(labels=['reviewCreatedVersion'], axis=1)
df['ReviewDATE']=df['TimeSTAMP'].dt.date 





# df.columns
today = date.today()
YD= today - timedelta(1)

df = df.loc[df['ReviewDATE']==YD]

df = df.drop(labels = ['reviewId', 'userImage', 'ReviewDATE'], axis=1)

# Data Frame copy to new data frame
full_dataset = df.copy()


df = df.loc[df['Rating']<=3]


# Translate to english 

trans = google_translator()
contents = df['ReviewText'].tolist()

if len(contents) == 0: 
    contents = 'Review notFound'

eng_TRANS = trans.translate(contents)


# today = date.today()
# YD= today - timedelta(1)

# df = df.loc[df['at']==YD]
# df = df.loc[df['score']<3]

# trans = google_translator()
# contents = df['content'].tolist()
# eng_TRANS = trans.translate(contents)

# df = df.drop(labels = ['reviewId', 'userImage'], axis=1)

# nlp = English()
# my_doc =  nlp(eng_TRANS)

# token_list = []
# for token in my_doc:
#     token_list.append(token.text)

# # Create list of word tokens after removing stopwords
# filtered_sentence =[] 

# for word in token_list:
#     lexeme = nlp.vocab[word]
#     if lexeme.is_stop == False:
#         filtered_sentence.append(word) 

# filtered_sentence = " ".join(filtered_sentence)
mask = np.array(Image.open(path.join("cloud.png")))

text = eng_TRANS


# Word Cloud Generate

wc = WordCloud(background_color="white",
                   mask=mask,
                   stopwords = STOPWORDS
               )

# generate wordcloud
asd = wc.generate(text)

# plt.figure(figsize = (8, 8), facecolor = None)
# plt.imshow(asd)
# plt.axis("off")
# plt.tight_layout(pad = 0)
# plt.show()

# Current Date 
current_date = date.today()
current_date = current_date - timedelta(1)
current_date = str(current_date)

# Word Cloud to image Convert 
result = asd.to_file(path.join(current_date+ " " +"play_store_review_wordCloud.png"))


#File save to excle file

file_name =  current_date
# plt.savefig('play_store_review_wordCloud.jpg')
full_dataset.to_excel(file_name + " " +'review_details.xlsx')

#Telegram file send 

# bot = telepot.Bot('1889724708:AAGMEuBjISKhwI0lM76uSpe06NLfb1stOWc')
# bot.sendPhoto(-1001404973022, photo=open(current_date+ " " +"play_store_review_wordCloud.png", 'rb'), caption='Translated Wrodcloud for Negative Playstore Reviews Date: '+ current_date)
# bot.sendDocument(-1001404973022, document=open(file_name + " " +'review_details.xlsx', 'rb'), caption='Detailed file for Negative Playstore Reviews Date: '+ current_date)

time.sleep(3)

# File remove
os.remove(file_name + " " +'review_details.xlsx')
os.remove(current_date+ " " +"play_store_review_wordCloud.png")

