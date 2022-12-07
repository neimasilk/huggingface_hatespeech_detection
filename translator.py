# !pip install googletrans==4.0.0rc1
from googletrans import Translator
def translate_tweet_to_javanese(tweet):
    translator = Translator()
    my_translation = translator.translate(tweet, src='en', dest='jw')
    return my_translation.text

def main():
    # test
    tweet = "The shit just blows me..claim you so faithful and down for somebody but still fucking with hoes! &#128514;&#128514;&#128514;"
    print(translate_tweet_to_javanese(tweet))

if __name__ == '__main__':
    main()

