from googletrans import Translator

wservice = []
with open('./preprocessing/googledomain.txt', "r") as f:
    for gdomain in f:
        line = 'translate.'+gdomain
        wservice.append(line.strip())

def translate_tweet_to_javanese(tweet, servis):
    translator = Translator(service_urls=[servis])
    my_translation = translator.translate(tweet,  src='en', dest='jw')
    return my_translation.text


for servis in wservice:
    print(servis)
    try:
      hasil = translate_tweet_to_javanese("hi my name is amien",servis)
    except:
      break
    print(hasil)

print(servis + " gagal!")