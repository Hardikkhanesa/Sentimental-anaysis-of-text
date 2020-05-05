from pymongo import MongoClient
from datetime import datetime, timedelta
import psycopg2, pytz


# mongodb connection
client = MongoClient('mongodb://localhost:27017')
db = client.TweetScraper

try:
    conn = psycopg2.connect(host="localhost", database="tweetdb", user="postgres", password="postgres")
except:
    print("DB Connection Failed")

cursor = conn.cursor()

# collection which are needed
tweets = db.tweet


# query to find average those have previous date and same local_ID
query = [{'$match': {'date': datetime.strftime(datetime.now() - timedelata(1) , '%Y-%m-%d')}}, {'$group': {'_id': {'local_ID': '$local_ID', 'date': '$date'}, 'sentimentAverage': {'$avg': '$sentiment'}}}]
# query = [{'$group': {'_id': {'local_ID': '$local_ID', 'date': '$date'}, 'sentimentAverage': {'$avg': '$sentiment'}}}]

# inserting every document into db
avg = tweets.aggregate(query)

for every in avg:
    print(every)
    # entry = DateWiseSentiment(local_ID=every['_id']['local_ID'], date=every['_id']['date'], sentimentAverage=every['sentimentAverage'])
    date = datetime.strptime(every['_id']['date'], '%Y-%m-%d')
    cursor.execute("INSERT INTO myapi_datewisesentiment (local_id_id, date, sentiment_average) VALUES (%s, %s, %s)", (every['_id']['local_ID'], date, every['sentimentAverage']))
    conn.commit()
