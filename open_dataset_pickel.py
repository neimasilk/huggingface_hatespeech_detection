import pickle

with open('hate_speech18_javanese.pickle', 'rb') as pickle_file:
  train_text_javanese = pickle.load(pickle_file)

# print(train_text_javanese) in good shape
import pandas as pd

# Load train_text_javanese into a pandas DataFrame
df = pd.DataFrame(train_text_javanese, columns=['Tweet', 'Label'])

print(df.head(50))
