import tweepy
import re
import pandas as pd
import csv

api_keys = "yHakB7BN5n9ShACkOizurIjD1"
api_secret_keys = "uFilFEmC75p7zBJaqVK28wY69nFVWTTH5r4J8pwRshQJMoKLCz"
access_token = "1223751810206191616-BE1H4UNlwEdn4DupnpUbCQ5gSrcrGF"
access_token_secret = "e3Ek3BhDJsdhQahAteWaIgW7YSxqzDCNWlHMXQE37VOs6"

auth = tweepy.OAuthHandler(api_keys, api_secret_keys)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

key_word = "vaksin"

csvFile = open(key_word+".csv","a+", newline = "", encoding="utf-8")
csvWriter = csv.writer(csvFile)

#membuat list kosong untuk menampung tanggal dibuatnya tweet, id, username, dan isi tweet
date = []
user_id = []
user_name = []
tweet_text = []

# #mencari tweet berdasarkan id user
# hasil_user = api.user_timeline(id="jokowi", count=5)
# #mencari tweet berdasarkan kata kunci
# hasil_search = api.search(q="covid", lang="id", count=5)

# for tweet in hasil_user:
#     print("\n")
#     print(tweet.text)
#     print("\n")

for tweet in tweepy.Cursor(api.search,q=key_word,count=1000, lang="id",since="2021-05-01", until="2021-05-02").items():
    print(tweet.created_at, tweet.id, tweet.user.name, tweet.text)
    date.append(tweet.created_at)
    user_id.append(tweet.id)
    user_name.append(tweet.user.name)
    tweet_text.append(tweet.text.encode("utf-8"))
    tweets = [tweet.created_at, tweet.id, tweet.user.name, tweet.text.encode("utf-8")]
    csvWriter.writerow(tweets)

dictTweets = {"waktu":date, "id":user_id, "user_name":user_name, "tweet":tweet_text}
df = pd.DataFrame(dictTweets, columns=["waktu", "id", "user_name", "tweet"])
df