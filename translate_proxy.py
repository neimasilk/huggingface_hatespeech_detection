from googletrans import Translator
import concurrent.futures
import re
import pickle
import random
import transformers
from datasets import load_dataset
from tqdm import tqdm
from tweet_cleanup import clean_tweets

def extract_proxy(address):
    return 'http://' + address.split()[-1].replace('>', '')


def translate_tweet_to_javanese_proxy(tweet,proxy):
    wservice = []
    with open('googledomain.txt', "r") as f:
        for gdomain in f:
            line = 'translate.'+gdomain
            wservice.append(line.strip())
    translator = Translator(service_urls=wservice, proxies=proxy)

    my_translation = translator.translate(tweet,  src='en', dest='jw')
    return my_translation.text

def find_translate_proxy(proxy_file='good_proxy_list.txt'):
    proxy_list = []
    working_proxy = []
    with open(proxy_file, "r") as f:  # file proxynya: proxies.txt
        for line in f:
            proxy_list.append(line)
        f.close()

    for alamat in proxy_list:
        try:
            proks = extract_proxy(alamat)
            prox_dict = {"http": proks}
            item = "Hi my name is Amien"
            translation = translate_tweet_to_javanese_proxy(item, prox_dict)
            working_proxy.append(alamat)
            print(translation)

        except Exception as e:
            print(str(e))
            continue
    # percobaan

    return working_proxy


def save_working_proxy():
    list_working_proxy = find_translate_proxy()
    with open('working_proxy.txt', 'w') as f:
        for item in list_working_proxy:
            f.write("%s" % item)

# import tqdm

def translate_tweet_to_javanese(tweet):
    array = []
    working_proxy = []
    with open('working_proxy.txt', "r") as f:  # file proxynya: proxies.txt
        for line in f:
            array.append(line)
        f.close()
    alamat = random.choice(array)
    try:
        proks = extract_proxy(alamat)
        prox_dict = {"http": proks}
        item = tweet
        translation = translate_tweet_to_javanese_proxy(item, prox_dict)
        working_proxy.append(alamat)
        return translation

    except Exception as e:
        print(str(e))

def main():
    # test
    datasets1 = load_dataset('hate_speech18')
    train_texts, train_labels = datasets1['train']['text'], datasets1['train']['label']

    train_texts = clean_tweets(train_texts)
    len(train_texts)
    train_text_javanese = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=40) as executor:
        for tweet in tqdm(executor.map(translate_tweet_to_javanese, train_texts), total=len(train_texts)):
            train_text_javanese.append(tweet)


    train_texts_label = list(zip(train_text_javanese, train_labels))
    # import pickle
    with open('hate_speech18_javanese.pickle', 'wb') as handle:
        pickle.dump(train_texts_label, handle, protocol=pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    main()
