from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import pickle

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client.TweetScraper
tweets = db.tweet

with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
loaded_CNN_model = load_model('avi-CNN_best_weights.02-0.8329.hdf5')

def predict_sentiment(text):
    pre_val = tokenizer.texts_to_sequences(text)
    pre_val_seq = pad_sequences(pre_val, maxlen=400)
    return loaded_CNN_model.predict(pre_val_seq)


for post in tweets.find({'sentiment': 0}):
    arr = [post['text']]
    sentiment_value = predict_sentiment(arr)
    query = {'ID': post['ID']}
    new_value = {"$set": {"sentiment": float(sentiment_value[0][0])}}
    tweets.update_one(query, new_value)


