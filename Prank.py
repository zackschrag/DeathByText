import sys
import datetime, threading
from api_info import API_CONF
from SMSClient import SMSClient
from TwitterClient import TwitterClient

# python Prank.py toNumber hashtag frequency number_of_texts
HASHTAG = sys.argv[2]
FREQUENCY = int(sys.argv[3])
NUMBER_OF_TEXTS = int(sys.argv[4])

def runPrank(argList):
    count = argList[0]
    twitterClient = argList[1]
    smsClient = argList[2]
    hashtag = argList[3]
    freq = argList[4]
    number_of_texts = argList[5]

    if (count > number_of_texts):
        return

    latestTweet = twitterClient.getTweets(hashtag)
    smsClient.sendSMS(latestTweet)
    count = count+1
    args = [count, twitterClient, smsClient, hashtag, freq, number_of_texts]
    threading.Timer(freq, runPrank, [args]).start()

twitterClient = TwitterClient(
    API_CONF['API_KEY'],
    API_CONF['API_SECRET'],
    API_CONF['ACCESS_TOKEN'],
    API_CONF['ACCESS_TOKEN_SECRET'])

smsClient = SMSClient(
    sys.argv[1],
    API_CONF['FROM_NUMBER'],
    API_CONF['TWILIO_SID'],
    API_CONF['TWILIO_TOKEN'])

runPrank([0, twitterClient, smsClient, HASHTAG, FREQUENCY, NUMBER_OF_TEXTS])