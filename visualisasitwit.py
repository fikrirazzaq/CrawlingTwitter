import json
import pandas as pd
import matplotlib.pyplot as plt

tweets_data_path = "krolingtwitter.txt"

# Bikin ArrayList buat nampung twit yg di crawling
tweets_data = []

# Ngebuka file txt
tweets_file = open(tweets_data_path, "r")

# Masukin tiap twit ke Arraylist tweets_data
for baris in tweets_file:
    try:
        tweet = json.loads(baris)
        tweets_data.append(tweet)
    except:
        print "Error Euuuuuuy"
        continue

# Nge-output-in jumlah twit yg di-crawling
print len(tweets_data)

twitsDataSet = pd.DataFrame()

twitsDataSet['text'] = map(lambda tweet: tweet['text'], tweets_data)
twitsDataSet['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
twitsDataSet['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)

# Ngitung jumlah bahasa dari seluruh twit yg dikrowl
twit_by_lang = twitsDataSet['country'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Bahasa', fontsize=15)
ax.set_ylabel('Jumlah Twit' , fontsize=15)
ax.set_title('4 Bahasa terbanyak', fontsize=15, fontweight='bold')

twit_by_lang[:4].plot(ax=ax, kind='bar', color='yellow')
plt.show()
