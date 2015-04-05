import sys
import datetime, threading
from api_info import API_CONF
from SMSClient import SMSClient
from TwitterClient import TwitterClient

# python Prank.py toNumber hashtag
def runPrank(argList):
    count = argList[0]
    twitterClient = argList[1]
    smsClient = argList[2]
    hashtag = argList[3]

    if (count == 1):
        return

    latestTweet = twitterClient.getTweets(hashtag)
    smsClient.sendSMS(latestTweet)
    count = count+1
    args = [count, twitterClient, smsClient, hashtag]
    threading.Timer(10, runPrank, [args]).start()

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

runPrank([0, twitterClient, smsClient, sys.argv[2]])