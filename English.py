from os import path
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
#dataset open
# file = open("Dataset/englishText.txt", "r", encoding='UTF-8')
# text = file.read()
text = "Professor Dr. Mohammad Delwar Hossain said that the patient that improves how improves its condition after the treatment of its asthma and high blood pressure is 53 years old, he said it can not be said that his treatment has been treated for long-term medical treatment Just a few days"

# create numpy araay for wordcloud mask image
# mask = np.array(Image.open(path.join("cloud.png")))


#create wordcloud object
wc = WordCloud(background_color="white",
                   #mask=mask,
                   stopwords = STOPWORDS
               )

# generate wordcloud
asd = wc.generate(text)

# plt.figure(figsize = (8, 8), facecolor = None)
# plt.imshow(asd)
# plt.axis("off")
# plt.tight_layout(pad = 0)
# plt.show()
# save to wordcloud image
result = asd.to_file(path.join("wordCloudEnglish12.png"))
import telepot
bot = telepot.Bot('1889724708:AAGMEuBjISKhwI0lM76uSpe06NLfb1stOWc')
bot.sendPhoto(1167757027, photo=open('wordCloudEnglish12.png', 'rb'))