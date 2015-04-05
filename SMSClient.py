from twilio.rest import TwilioRestClient

class SMSClient:
    account_sid = ""
    auth_token  = ""
    client = None

    toNumber = ""
    fromNumber = ""

    def __init__(self, toNum, fromNum, sid, token):
        self.toNumber = toNum
        self.fromNumber = fromNum
        self.account_sid = sid
        self.auth_token = token
        self.client = TwilioRestClient(self.account_sid, self.auth_token)

    def sendSMS(self, messageBody):
        message = self.client.messages.create(body=messageBody,
            to = self.toNumber,
            from_ = self.fromNumber)
