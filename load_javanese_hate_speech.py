import transformers
from datasets import load_dataset

# datasets1 = load_dataset('hate_speech18')

# import IPython; IPython.embed(); exit(1)
# train_texts, train_labels = datasets1['train']['text'], datasets['train']['label']
# 0 = no hate speech
# 1 = hate speech



# datasets2 = load_dataset('hate_speech_offensive')
# get list of class and tweet
# import IPython; IPython.embed(); exit(1)

#0 = hate speech
#1 = offensive language
#2 = neither

# train_texts, train_labels_class = datasets2['train']['tweet'], datasets2['train']['class']
# train_labels = [0 if x == 2 else 1 for x in train_labels_class]

# datasets3 = load_dataset('tweets_hate_speech_detection')
# get list of class and tweet
# import IPython; IPython.embed(); exit(1)
# train_texts, train_labels = datasets3['train']['tweet'], datasets['train']['label']


import pandas as pd

# Load the dataset into a pandas DataFrame
df = pd.read_csv("indo_hate.csv", delimiter="\t",encoding="ISO-8859-1")

# Print the first few rows of the DataFrame
train_texts = df["Tweet"].tolist()
train_label_text = df["Label"].tolist()
train_labels = [0 if x == "Non_HS" else 1 for x in train_label_text]

# a = ["nol", "satu", "nol", "nol"]
# b = [int(x) if x == "nol" else 1 for x in a]

# import IPython; IPython.embed(); exit(1)



