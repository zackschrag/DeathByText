# DeathByText

Usage: python Prank.py phoneNumber hashtag frequency number_of_texts

For example, if the user command was:
python Prank.py 1112223333 YOLO 5 10

The phone number: 1112223333 would receive the latest tweet using #YOLO every 5 seconds, 10 times.

Note: In order to run this properly, you need a file called api_info.py with this in it:

API_CONF = {
	'API_KEY': "key",
	'API_SECRET': "secret",
	'ACCESS_TOKEN': "token",
	'ACCESS_TOKEN_SECRET': "token secret",
	'TWILIO_SID': "twilio sid",
	'TWILIO_TOKEN': "twilio token",
	'FROM_NUMBER': "number"
}

