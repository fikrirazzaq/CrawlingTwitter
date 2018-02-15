from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key = "zXsE3S1UkK7KewzMnEB2Vt9Yh"
consumer_secret = "l7Phs6CQOpI0q0o6TgWuq1kKT0PWPRaIPZV3RnN7KVNNOqPNDe"
access_token = "84281545-8QHMJk7wDZ9uX1l7C1DH756OHS9LFWj8GBziPgPhZ"
access_token_secret = "NvMIwyJkdMj8Yqj0pCbFqlZmqweUoCof1R754U7Smr9hL"

# Kelas sebagai listener yg nantinya ngeoutputin twit-twit di konsol
class StdOutListener(StreamListener):
    
    def on_data(self, data):
        print data
        return True
    
    def on_error(self, status):
        print status


if __name__ == '__main__':
    
    # Menangani otentifikasi twitter & koneksi ke Stream API Twitter
    listen = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listen)

    stream.filter(track=['juventus', 'barcelona', 'chelsea', 'persib'])


