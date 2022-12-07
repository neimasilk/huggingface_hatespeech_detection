import re
# clean up one tweet
def clean_tweet(tweet):
    tweet = tweet.lower()
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)
    tweet = re.sub('@[^\s]+', 'AT_USER', tweet)
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    tweet = tweet.strip('\'"')
    return tweet

# clean up a list of tweets
def clean_tweets(tweets):
    return [clean_tweet(tweet) for tweet in tweets]


def main():
    # test
    tweet = "The shit just blows me..claim you so faithful and down for somebody but still fucking with hoes! &#128514;&#128514;&#128514;"
    print(clean_tweet(tweet))
if __name__ == '__main__':
    main()
